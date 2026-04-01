# Angebotserstellung – Datenanforderungen & digitale Erfassung

**Kontext:** Handwerksbetriebe (Sanitär, Maler, Elektriker, Fliesenleger)
**Erfassungskanal:** Hausbesuch beim Kunden (mobil, Tablet/Smartphone)
**Output:** Internes Kalkulationsblatt + Kundenangebot (PDF)

---

## 1. Informationsstruktur

### 1.1 Kundendaten

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Vorname, Nachname | Ja | Text | Eingabe |
| Straße, Hausnummer, PLZ, Ort | Ja | Text / Autovervollständigung | Eingabe |
| Telefonnummer | Ja | Tel | Eingabe |
| E-Mail-Adresse | Nein | E-Mail | Eingabe |
| Ansprechpartner (bei Gewerbe) | Nein | Text | Eingabe |
| Firmenname (bei Gewerbe) | Nein | Text | Eingabe |
| Rechnungsadresse abweichend? | Nein | Bool + Felder | Checkbox + Eingabe |

---

### 1.2 Auftragsgrunddaten

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Gewerk | Ja | Enum | Auswahl (Sanitär / Maler / Elektriker / Fliesenleger / Sonstiges) |
| Auftragsart | Ja | Enum | Auswahl (Neubau / Sanierung / Reparatur / Wartung / Erweiterung) |
| Kurzbezeichnung des Auftrags | Ja | Text | Freitext, max. 120 Zeichen |
| Ausführungsadresse (= Kundenadresse?) | Ja | Bool + Felder | Checkbox "gleich wie Kundenadresse" oder separate Eingabe |
| Raum / Bereich | Nein | Text | Freitext (z.B. "Bad EG", "Wohnzimmer") |
| Detaillierte Leistungsbeschreibung | Ja | Langer Text | Freitext / Diktat |
| Fotos der Situation vor Ort | Nein* | Bild(er) | Kamera-Upload (min. empfohlen: 2 Fotos) |

> *Fotos sind technisch optional, aber für Kalkulation und Dokumentation dringend empfohlen.

---

### 1.3 Maße & technische Details (gewerkeabhängig)

Das Formular zeigt jeweils nur die relevanten Felder basierend auf dem gewählten Gewerk.

#### Sanitär
| Feld | Pflicht | Typ |
|---|---|---|
| Anzahl Sanitärobjekte (WC, Waschbecken, Dusche, Wanne, ...) | Ja | Zähler je Typ |
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
| Fliesenmaterial (Keramik, Feinsteinzeug, Naturstein, ...) | Ja | Auswahl |
| Alten Belag entfernen? | Ja | Bool |
| Estrich / Abdichtung erforderlich? | Nein | Bool |
| Verlegemuster (Standard, Diagonal, Fischgrät, ...) | Nein | Auswahl |
| Fliesenschnitte aufwändig? (viele Ecken, Rundungen) | Nein | Bool |
| Fugenmaterial / Fugenfarbe | Nein | Auswahl |

---

### 1.4 Kundenwünsche & Qualitätsniveau

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Qualitätsniveau | Ja | Enum | Auswahl: Basis / Standard / Premium |
| Markenpräferenz / Material-Wunsch | Nein | Text | Freitext |
| Konkrete Produkt-/Modellwünsche | Nein | Text | Freitext |
| Besondere Anforderungen (Barrierefreiheit, Allergie, ...) | Nein | Text | Freitext |
| Hinweise zur Zugänglichkeit / Bausituation | Nein | Text | Freitext |

---

### 1.5 Budget & Zeitrahmen

| Feld | Pflicht | Typ | Erfassung |
|---|---|---|---|
| Budgetrahmen des Kunden (€) | Nein | Zahl (Bereich: von – bis) | Eingabe oder Schieberegler |
| Budgetrahmen ist verbindlich? | Nein | Bool | Checkbox |
| Gewünschter Ausführungsbeginn | Nein | Datum | Datumsauswahl |
| Gewünschte Fertigstellung bis | Nein | Datum | Datumsauswahl |
| Terminflexibilität vorhanden? | Nein | Bool | Checkbox |
| Besichtigungstermin / Aufmaßtermin erforderlich? | Nein | Bool | Checkbox |

---

## 2. Übersicht: Pflichtfelder

Folgende Felder sind **zwingend erforderlich**, um ein Angebot zu erzeugen:

1. Name + Adresse des Kunden
2. Telefonnummer
3. Gewerk
4. Auftragsart
5. Kurzbezeichnung des Auftrags
6. Ausführungsadresse
7. Leistungsbeschreibung
8. Mindestens **ein gewerke­spezifisches Maßfeld** (z.B. m² oder Anzahl Objekte)
9. Qualitätsniveau

---

## 3. Digitale Erfassung beim Hausbesuch

### 3.1 Gerät & Modus
- **Gerät:** Tablet (bevorzugt) oder Smartphone
- **Modus:** Progressive Web App (PWA) oder native App
- **Offline-Fähigkeit:** Ja – Daten werden lokal gespeichert und synchronisiert, sobald Verbindung besteht

### 3.2 Erfassungsreihenfolge (Wizard / Schritt-für-Schritt)

```
Schritt 1: Kundendaten
   → Autovervollständigung via Adress-API (z.B. Google Places)
   → Bestandskunde? → vorausfüllen aus Kundendatenbank

Schritt 2: Auftragsgrundlage
   → Gewerk wählen → passendes Unterformular erscheint dynamisch

Schritt 3: Maße & technische Details
   → Gewerke­spezifisches Formular
   → Fotos aufnehmen (Kamera direkt im Formular)
   → Spracheingabe für Beschreibungsfelder (optional)

Schritt 4: Kundenwünsche
   → Qualitätsniveau, Materialwünsche, Sonderwünsche

Schritt 5: Budget & Zeitrahmen
   → Optional, aber empfohlen

Schritt 6: Zusammenfassung & Bestätigung
   → Alle Eingaben anzeigen
   → Digitale Unterschrift des Kunden (optional)
   → Speichern / An Büro senden
```

### 3.3 Unterstützende Eingabehilfen

| Feature | Beschreibung |
|---|---|
| Kamera-Integration | Fotos direkt im Formular aufnehmen und speichern |
| Spracheingabe | Beschreibungsfelder per Diktat ausfüllen |
| Adress-Autovervollständigung | Reduziert Tippfehler bei Adressen |
| Bestandskunden-Suche | Kundendaten aus vorherigen Aufträgen laden |
| Vorlagen / Schnellauswahl | Häufige Auftragstypen als vorbefüllte Vorlagen |
| Offline-Modus | Vollständige Erfassung auch ohne Internetverbindung |
| Digitale Unterschrift | Kundenunterschrift auf dem Tablet |

---

## 4. Datenfluss nach der Erfassung

```
Vor-Ort-Erfassung (Tablet)
        ↓
Lokale Zwischenspeicherung
        ↓ (bei Netz)
Synchronisation mit Backend
        ↓
Automatische Kalkulation
        ↓
    ┌───┴───┐
    ↓       ↓
Interne    Kunden-
Kalkul.    Angebot
(intern)   (PDF)
```

---

## 5. Offene Fragen / Klärungsbedarf

- [ ] Sollen Materialkosten direkt aus einem Lieferantenkatalog/-preisliste gezogen werden?
- [ ] Welche Gewinnmarge / Stundensatzstruktur liegt der Kalkulation zugrunde?
- [ ] Gibt es mehrere Mitarbeiter, die Angebote erstellen (Mehrbenutzer)?
- [ ] Soll der Kunde das Angebot digital per E-Mail erhalten und digital annehmen können?
- [ ] Bestehende Software (z.B. Buchhaltung, CRM) an die das Tool angebunden werden soll?
