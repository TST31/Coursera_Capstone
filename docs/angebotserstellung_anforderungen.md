# Angebotserstellung – Datenanforderungen & digitale Erfassung

**Kontext:** Handwerksbetriebe (Sanitär, Maler, Elektriker, Fliesenleger)
**Erfassungskanal:** Hausbesuch beim Kunden (mobil, Tablet/Smartphone)
**Output:** Internes Kalkulationsblatt + Kundenangebot (PDF, digital annehmbar)

---

## Architekturprinzip: Drei Datenebenen

Das System unterscheidet strikt zwischen Daten, die **einmalig** hinterlegt werden, und solchen, die **pro Auftrag** erfasst werden. Nur die dritte Ebene wird beim Hausbesuch abgefragt.

```
┌─────────────────────────────────────────────────────────┐
│  Ebene 1: BETRIEBSPROFIL                                │
│  (einmalig pro Betrieb, im Back-Office konfiguriert)    │
│  Gewerk, Stundensätze, Marge, Firmendaten, Logo ...     │
├─────────────────────────────────────────────────────────┤
│  Ebene 2: KUNDENDATENBANK                               │
│  (einmalig pro Kunde, danach wiederverwendet)           │
│  Name, Adresse, Kontakt, Kundenhistorie ...             │
├─────────────────────────────────────────────────────────┤
│  Ebene 3: AUFTRAGSDATEN                                 │
│  (pro Angebot, Erfassung beim Hausbesuch)               │
│  Maße, Beschreibung, Wünsche, Budget, Fotos ...         │
└─────────────────────────────────────────────────────────┘
```

> **Ziel:** Beim Hausbesuch werden nur noch Ebene-3-Daten abgefragt. Alles andere ist bereits vorhanden oder wird automatisch aus dem Profil übernommen.

---

## 1. Betriebsprofil (Ebene 1)

Wird **einmalig** vom Betrieb im Back-Office eingerichtet. Alle Einstellungen sind pro Betrieb individuell konfigurierbar. Mehrere Betriebe können das System parallel nutzen (Mandantenfähigkeit).

### 1.1 Unternehmensdaten

| Feld | Pflicht | Typ |
|---|---|---|
| Firmenname | Ja | Text |
| Rechtsform (GmbH, GbR, Einzelunternehmen, ...) | Ja | Enum |
| Adresse, PLZ, Ort | Ja | Text |
| Telefon, E-Mail, Website | Ja | Text |
| Firmenlogo | Nein | Bild (PNG/SVG) |
| Steuernummer / USt-IdNr. | Ja | Text |
| IBAN / Bankverbindung | Nein | Text |
| Angebots-Gültigkeitsdauer (Tage) | Ja | Zahl (Standard: 30) |

### 1.2 Gewerk-Konfiguration

Ein Betrieb kann **ein oder mehrere Gewerke** aktivieren. Pro aktiviertem Gewerk werden eigene Einstellungen hinterlegt.

| Feld | Pflicht | Typ |
|---|---|---|
| Aktive Gewerke | Ja | Mehrfachauswahl (Sanitär / Maler / Elektriker / Fliesenleger / Sonstiges) |
| Standard-Gewerk (bei Angebotserstellung vorausgewählt) | Nein | Enum aus aktiven Gewerken |

### 1.3 Stundensätze & Kalkulation (pro Gewerk, konfigurierbar)

| Feld | Pflicht | Typ | Hinweis |
|---|---|---|---|
| Arbeitsstundensatz (€/h, netto) | Ja | Zahl | Wird nicht im Kundenangebot gezeigt |
| Fahrkostenpauschale | Nein | Zahl (€ pauschal oder €/km) | |
| Materialaufschlag (%) | Nein | Zahl | Vorbereitet, aktuell manuell |
| Standard-Gewinnmarge (%) | Nein | Zahl | Pro Betrieb individuell |
| Mindestauftragswert (€) | Nein | Zahl | |
| Lieferantenkatalog verknüpft | Nein | Bool | Vorbereitet für spätere Integration |

> **Hinweis Lieferantenkatalog:** Die Datenstruktur ist vorbereitet. Bis zur Kataloganbindung werden Materialkosten manuell pro Angebot eingegeben oder pauschal geschätzt.

### 1.4 Angebotsvorlagen & Texte

| Feld | Pflicht | Typ |
|---|---|---|
| Angebots-Einleitungstext | Nein | Langer Text |
| Angebots-Schlusstext / AGB-Hinweis | Nein | Langer Text |
| Zahlungsbedingungen | Nein | Text (z.B. "14 Tage netto") |
| Vorlagen für häufige Leistungspositionen | Nein | Liste von Textbausteinen |

### 1.5 Benutzer & Zugriffsrechte

| Feld | Pflicht | Typ |
|---|---|---|
| Benutzer (Name, E-Mail, Rolle) | Ja (min. 1) | Liste |
| Rolle | Ja | Enum: Admin / Monteur / Büro |
| Monteur darf Angebote erstellen? | Ja | Bool (pro Rolle) |
| Kalkulation / Marge sichtbar? | Ja | Bool (pro Rolle) – Standard: Nein, freischaltbar |

---

## 2. Kundendatenbank (Ebene 2)

Wird **einmalig pro Kunde** angelegt und bei jedem Folgeauftrag wiederverwendet. Beim Hausbesuch reicht eine Suche nach Name oder Telefonnummer – alle Felder werden vorausgefüllt.

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Vorname, Nachname | Ja | Text | Eingabe (einmalig) |
| Straße, Hausnummer, PLZ, Ort | Ja | Text / Autovervollständigung | Eingabe (einmalig) |
| Telefonnummer | Ja | Tel | Eingabe (einmalig) |
| E-Mail-Adresse | Nein | E-Mail | Eingabe (einmalig) |
| Ansprechpartner (bei Gewerbe) | Nein | Text | Eingabe (einmalig) |
| Firmenname (bei Gewerbe) | Nein | Text | Eingabe (einmalig) |
| Rechnungsadresse abweichend? | Nein | Bool + Felder | Checkbox + Eingabe |
| Notizen zum Kunden | Nein | Text | Freitext |
| Auftragshistorie | – | Automatisch | Systemseitig gepflegt |

---

## 3. Auftragsdaten (Ebene 3) – Erfassung beim Hausbesuch

Diese Daten werden **pro Angebot** neu erfasst. Das sind die einzigen Informationen, die beim Hausbesuch aktiv abgefragt werden.

### 3.1 Auftragsgrunddaten

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Kunde | Ja | Suche / Neu | Bestandskunde suchen oder neu anlegen |
| Gewerk | Ja | Enum | Vorausgewählt aus Betriebsprofil, änderbar |
| Auftragsart | Ja | Enum | Neubau / Sanierung / Reparatur / Wartung / Erweiterung |
| Kurzbezeichnung des Auftrags | Ja | Text | Freitext, max. 120 Zeichen |
| Ausführungsadresse | Ja | Bool + Felder | Checkbox "gleich wie Kundenadresse" oder separat |
| Raum / Bereich | Nein | Text | z.B. "Bad EG", "Wohnzimmer" |
| Leistungsbeschreibung | Ja | Langer Text | Freitext / Diktat |
| Fotos der Situation vor Ort | Nein* | Bild(er) | Kamera direkt im Formular |

> *Fotos sind technisch optional, für Dokumentation und Streitvermeidung aber dringend empfohlen.

### 3.2 Maße & technische Details (gewerkeabhängig, dynamisches Formular)

#### Sanitär
| Feld | Pflicht | Typ |
|---|---|---|
| Anzahl Sanitärobjekte (WC, Waschbecken, Dusche, Wanne ...) | Ja | Zähler je Typ |
| Rohrleitungsart (Kalt-, Warmwasser, Abwasser) | Ja | Mehrfachauswahl |
| Geschätzte Rohrleitungslänge (m) | Ja | Zahl |
| Unterputz / Aufputz | Ja | Enum |
| Fliesen demontieren erforderlich? | Nein | Bool |
| Material-Präferenz (Kupfer, Edelstahl, Kunststoff) | Nein | Auswahl |

#### Maler
| Feld | Pflicht | Typ |
|---|---|---|
| Wandfläche gesamt (m²) | Ja | Zahl |
| Deckenfläche (m²) | Nein | Zahl |
| Raumhöhe (m) | Ja | Zahl |
| Aktuell tapeziert? | Ja | Bool |
| Tapete abziehen erforderlich? | Nein | Bool |
| Untergrundvorbereitung nötig? (spachteln, schleifen) | Nein | Bool |
| Farbwunsch / Stil | Nein | Text + Farbcode / Muster |
| Anzahl Anstriche | Ja | Zahl (Standard: 2) |

#### Elektriker
| Feld | Pflicht | Typ |
|---|---|---|
| Art der Arbeit (Neuinstallation, Erweiterung, Reparatur) | Ja | Enum |
| Anzahl Steckdosen / Schalter | Nein | Zahl |
| Kabelverlegung (Aufputz / Unterputz / Kabelkanal) | Ja | Enum |
| Anzahl Lichtpunkte | Nein | Zahl |
| Verteilerschrank: Erweiterung oder Neubau? | Nein | Bool + Enum |
| Absicherungsleistung (A) | Nein | Zahl |
| Mess-/Prüfprotokoll erforderlich? | Nein | Bool |

#### Fliesenleger
| Feld | Pflicht | Typ |
|---|---|---|
| Verlegefläche gesamt (m²) | Ja | Zahl |
| Wandfliesen (m²) | Nein | Zahl |
| Bodenfliesen (m²) | Nein | Zahl |
| Fliesenformat (cm × cm) | Ja | Text / Auswahl |
| Fliesenmaterial (Keramik, Feinsteinzeug, Naturstein ...) | Ja | Auswahl |
| Alten Belag entfernen? | Ja | Bool |
| Estrich / Abdichtung erforderlich? | Nein | Bool |
| Verlegemuster (Standard, Diagonal, Fischgrät ...) | Nein | Auswahl |
| Fliesenschnitte aufwändig? (viele Ecken, Rundungen) | Nein | Bool |
| Fugenmaterial / Fugenfarbe | Nein | Auswahl |

### 3.3 Kundenwünsche & Qualitätsniveau

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Qualitätsniveau | Ja | Enum | Basis / Standard / Premium |
| Markenpräferenz / Material-Wunsch | Nein | Text | Freitext |
| Konkrete Produkt-/Modellwünsche | Nein | Text | Freitext |
| Besondere Anforderungen (Barrierefreiheit ...) | Nein | Text | Freitext |
| Hinweise zur Zugänglichkeit / Bausituation | Nein | Text | Freitext |

### 3.4 Budget & Zeitrahmen

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Budgetrahmen des Kunden (€) | Nein | Zahl (von – bis) | Eingabe oder Schieberegler |
| Budgetrahmen ist verbindlich? | Nein | Bool | Checkbox |
| Gewünschter Ausführungsbeginn | Nein | Datum | Datumsauswahl |
| Gewünschte Fertigstellung bis | Nein | Datum | Datumsauswahl |
| Terminflexibilität vorhanden? | Nein | Bool | Checkbox |

---

## 4. Pflichtfelder beim Hausbesuch (Minimalanforderung für Angebotserstellung)

1. Kunde (Bestandskunde oder neu: Name + Adresse + Telefon)
2. Auftragsart
3. Kurzbezeichnung des Auftrags
4. Ausführungsadresse
5. Leistungsbeschreibung
6. Mindestens **ein gewerke­spezifisches Maßfeld**
7. Qualitätsniveau

> Gewerk und Firmendaten kommen automatisch aus dem Betriebsprofil – kein erneutes Abfragen.

---

## 5. Erfassungsablauf beim Hausbesuch (Wizard)

```
Schritt 1: Kunde
   → Bestandskunde suchen (Name / Tel) → Daten vorausfüllen
   → Oder: Neukunde anlegen

Schritt 2: Auftrag
   → Auftragsart, Kurzbezeichnung, Ausführungsadresse
   → Gewerk (aus Profil vorausgewählt, änderbar)

Schritt 3: Maße & Technisches
   → Dynamisches Formular je Gewerk
   → Fotos aufnehmen
   → Spracheingabe für Beschreibung

Schritt 4: Wünsche & Budget
   → Qualitätsniveau, Materialwünsche
   → Budget & Zeitrahmen (optional)

Schritt 5: Zusammenfassung
   → Alle Eingaben prüfen
   → Speichern & synchronisieren
```

### Eingabehilfen

| Feature | Beschreibung |
|---|---|
| Kamera-Integration | Fotos direkt im Formular |
| Spracheingabe | Freitextfelder per Diktat |
| Adress-Autovervollständigung | Fehlerreduktion bei Neueingabe |
| Bestandskunden-Suche | Schnellzugriff auf vorhandene Kundendaten |
| Vorlagen | Häufige Leistungspositionen als Textbausteine |
| Offline-Modus | Vollständige Erfassung ohne Internetverbindung |

---

## 6. Datenfluss

```
Betriebsprofil          Kundendatenbank
(Stundensätze,          (Name, Adresse,
 Marge, Gewerk ...)      Kontakt ...)
       │                       │
       └──────────┬────────────┘
                  ↓
         Auftragsdaten
         (Hausbesuch)
                  ↓
         Lokale Speicherung
                  ↓ (bei Netz)
         Synchronisation Backend
                  ↓
         Automatische Kalkulation
                  ↓
         ┌────────┴────────┐
         ↓                 ↓
    Interne            Kundenangebot (PDF)
    Kalkulation             ↓
    (rollenabhängig    ┌────┴────┐
     sichtbar)         ↓        ↓
                  E-Mail mit  Unterschrift
                  Bestät.-    auf Tablet
                  Link        vor Ort
```

---

## 7. Entscheidungen & offene Punkte

### Entschieden

| Thema | Entscheidung |
|---|---|
| Rollen & Datenzugriff | Kalkulation / Marge ist **nicht per Default sichtbar**, aber pro Rolle freischaltbar (voller Zugang möglich). Konfiguration im Betriebsprofil. |
| Digitale Angebotsannahme | **Beides:** (a) E-Mail mit Bestätigungslink an den Kunden, (b) direkte Unterschrift auf dem Tablet vor Ort. |

### Zur späteren Detaillierung

- **Kalkulationslogik:** Wie werden Arbeitsstunden aus Maßen und Auftragsart abgeleitet? (Richtwerte / Zeitansätze pro Gewerk – eigenes Konzept erforderlich)
- **Anbindung Buchhaltung / CRM:** Ob und welche Fremdsysteme angebunden werden sollen, ist noch offen.
