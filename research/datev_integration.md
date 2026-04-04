# DATEV-Integration: Optionen für Startups

> Stand: März 2026 | Quellen: developer.datev.de, datev.de/marktplatz, Candis, Dext, Lexware

---

## 1. DATEV-Marktplatz-Partnerprogramm

### Was ist der DATEV-Marktplatz?

Der DATEV-Marktplatz ist ein Ökosystem, auf dem Software-Hersteller ihre Lösungen listen können, die DATEV-Produkte sinnvoll ergänzen. Partnerlösungen sind über DATEV-Datenservices mit DATEV-Produkten verbunden und ermöglichen automatisierten, sicheren Datenaustausch zwischen der Drittanwendung und DATEV Kanzleisoftware / DATEV Unternehmen online.

### Partnertypen (seit 2023 neue Bezeichnungen)

| Partnertyp | Vorherige Bezeichnung | Voraussetzungen |
|------------|----------------------|-----------------|
| **DATEV-Marktplatz Premium Partner** | DATEV Software Partner | Vollständige Partnerschaft, höchste Anforderungen |
| **DATEV-Marktplatz Schnittstellen Partner** | Einfache Schnittstellen-Integration | Min. 25 aktive Kunden für den DATEV-Datenservice + 3 Referenzkunden |
| **DATEV Schnittstellen Anbieter** | Eigenständige Integration ohne Marktplatz-Listing | Technische Implementierung via Developer Portal |

### Voraussetzungen für DATEV-Marktplatz Schnittstellen Partner

1. **Mindest-Kundenzahl:** Der Hersteller muss seinen DATEV-Datenservice für **mindestens 25 Kunden** implementiert haben
2. **Referenzkunden:** 3 Referenzkunden müssen benannt werden
3. **Lohnschnittstelle (falls zutreffend):** Zusätzlich mindestens 25 Kunden für DATEV-Lohnaustausch und Bestätigung durch 3 Steuerberater, dass die Schnittstelle seit min. 3 Monaten korrekt genutzt wird
4. **Technische Prüfung:** DATEV prüft fehlerfreies Einlesen der Output-Datei (nicht fachliche Korrektheit)

### Zeitaufwand (Schätzung)

| Phase | Aufwand |
|-------|---------|
| Developer Portal Registrierung & API-Abonnement | 1–2 Tage |
| Sandbox-Zugang einrichten | 1–3 Tage |
| Technische Implementierung (MVP, 1 API) | 4–12 Wochen (je nach Komplexität) |
| 25 Pilot-Kunden aufbauen | 3–12 Monate |
| Partnerschaftsantrag + Prüfung durch DATEV | 4–8 Wochen |
| **Gesamt bis Marktplatz-Listing** | **~6–18 Monate** |

### Kosten

DATEV veröffentlicht keine öffentlichen Preise für das Partnerprogramm. Bekannte Kostenblöcke:
- API-Abonnement im Developer Portal (genaue Kosten: Anfrage erforderlich)
- Entwicklungskosten für Implementierung (intern oder extern)
- Laufende Lizenzgebühren (modellabhängig)

---

## 2. DATEV-API-Schnittstellen (Öffentliche Angebote)

### Übersicht der API-Typen

#### A) Dateibasierte Schnittstellen (File Interfaces)

| Format | Beschreibung | Ziel-System | Besonderheit |
|--------|-------------|-------------|-------------|
| **DATEV-Format (CSV)** | Standard-CSV mit Metadaten-Kopfzeile | DATEV Rechnungswesen | De-facto-Standard; keine Belegbilder |
| **DATEV XML-Schnittstelle online** | XML-basiert (UTF-8) | DATEV Unternehmen online | Mit Belegbildern; Import via DATEV Belegtransfer |
| **Traffiqx® Direct** | XML für SmartTransfer | DATEV SmartTransfer | Für Rechnungen, Gutschriften, Bestellungen |

**Wichtige Regel:**
- DATEV **Rechnungswesen** → **CSV**
- DATEV **Unternehmen online** → **XML**
- Kein freies Wählen zwischen den Formaten

#### B) Online-API-Datenservices

| Service | Beschreibung | Datentypen |
|---------|-------------|------------|
| **Belegbilderservice** | Überträgt PDF-Belege ohne Buchungsdaten | PDF-Dokumente |
| **Rechnungsdatenservice 1.0 (RDS)** | Überträgt strukturierte Daten + Belegbild | XML + PDF |
| **Buchungsdatenservice (BDS)** | Überträgt vollständige Buchungssätze | CSV (DATEV-Format) |
| **DATEV Lohnaustauschdatenservice** | Lohndaten-Übertragung | Lohnstammdaten |

### Authentifizierung

| Methode | Beschreibung |
|---------|-------------|
| **OAuth 2.0** | Moderner Standard für API-Zugriff |
| **Zertifikatsbasiert** | Komplex, höherer Einrichtungsaufwand |

### Besonderheit: Asynchrone Verarbeitung

Anders als REST-APIs mit sofortiger Antwort verarbeitet DATEV Batch-Jobs asynchron:
1. Job erstellen
2. Job starten
3. Status abfragen (Polling)
4. Ergebnis auswerten

→ Erhöhter Entwicklungsaufwand gegenüber modernen APIs.

### Exportformate im Überblick

| Format | Verwendung |
|--------|------------|
| **CSV** | Buchungsdaten für DATEV Rechnungswesen |
| **XML** | Belegdaten + Buchungen für DATEV Unternehmen online |
| **PDF** | Belegbilder (nur Belegbilderservice) |
| **SEPA-XML** | Zahlungsverkehr (z.B. via Candis SEPA-Export) |

---

## 3. Wie Candis DATEV integriert

Candis (DATEV-Marktplatz Premium Partner seit 2018) verwendet alle drei DATEV-Exporttypen:

### Schritt-für-Schritt-Integration

```
Beleg eingang (E-Mail, PDF, Scan)
         ↓
KI-gestützte OCR-Extraktion (99% Genauigkeit)
         ↓
Vorkontierung in Candis-Oberfläche
         ↓
Freigabe-Workflow (Approval)
         ↓
DATEV-Export (Auswahl je nach Setup):
  ├── Belegbilderservice → PDFs an DATEV UO
  ├── RDS 1.0 (XML) → Daten + Bild als Buchungsvorschlag
  └── BDS (CSV) → Vollständige Buchungssätze
         ↓
DATEV Unternehmen online / Kanzlei
```

**Dauerhafte Verbindung:** Candis unterhält eine permanente API-Verbindung zu DATEV Unternehmen online – kein manueller Export notwendig.

**Audit Trail:** Jeder Export enthält eine vollständige Prozessdokumentation.

**Technische Prüfung:** DATEV prüft regelmäßig die fehlerfreie Einlesung (nicht fachliche Korrektheit).

**Candis-Preise:** Ab ~369 €/Monat – zu teuer für Kleinstbetriebe, richtet sich an Mittelstand und Steuerberater.

---

## 4. Wie Dext DATEV integriert

**Befund:** Die DATEV-Integration von Dext für den deutschen Markt ist nicht eindeutig dokumentiert. Dext ist primär für angloamerikanische Systeme entwickelt (Xero, QuickBooks, Sage). Für DATEV-Integration in Deutschland ist explizite Verifikation bei dext.com/de notwendig.

**Dext-Technologie (unabhängig von DATEV):**
- OCR + KI-Extraktion mit 99,9% Genauigkeit
- Kategorisierungsvorschläge
- Sync mit 30+ Buchhaltungssystemen
- Bei tatsächlicher DATEV-Integration: wahrscheinlich über CSV-Export (DATEV-Format) oder API

---

## 5. Einfachere Alternativen zur direkten DATEV-Integration

### Option A: lexoffice/Lexware Office als Mittler

**Empfohlen für Startups in der Frühphase.**

```
Eigene App
    ↓ (Export/API)
lexoffice (Lexware Office)
    ↓ (DATEV Connect Online)
DATEV Unternehmen online / Kanzlei
```

**Vorteile:**
- lexoffice ist bereits DATEV-Marktplatz Partner
- Offiziell 2 DATEV-Services: DATEV Connect Online + Rechnungsdatenservice 1.0
- Integration über lexoffice-API möglich (REST-API)
- Kosten für den Endkunden: ab 5,95–9,95 €/Monat
- Keine eigene DATEV-Zertifizierung nötig

**Nachteile:**
- Abhängigkeit von lexoffice als Zwischenlayer
- Nutzer braucht lexoffice-Account zusätzlich zur eigenen App

### Option B: DATEV CSV-Export (einfachste Lösung)

```
Eigene App
    ↓
DATEV-Format CSV generieren
    ↓
Steuerberater importiert manuell in DATEV Rechnungswesen
```

**Vorteile:**
- Kein API-Abonnement, kein Zertifizierungsprozess
- DATEV-CSV ist öffentlich dokumentiert
- Schnell implementierbar (< 1 Woche Entwicklung)
- Funktioniert mit allen DATEV-Systemen

**Nachteile:**
- Kein automatischer Datenaustausch (manueller Steuerberater-Import)
- Keine Belegbilder im CSV
- Nicht für vollautomatischen Workflow geeignet

### Option C: DATEV XML-Export (mittlere Komplexität)

```
Eigene App
    ↓
XML + PDF generieren (DATEV XML-Format)
    ↓
Nutzer lädt in DATEV Belegtransfer hoch (Tool von DATEV)
    ↓
DATEV Unternehmen online
```

**Vorteile:**
- Belegbilder inklusive
- Kein API-Abonnement notwendig (Datei-Interface)
- Gut geeignet für vorbereitende Buchhaltung

**Nachteile:**
- Halbmanueller Prozess (Nutzer muss DATEV Belegtransfer bedienen)
- Höherer Entwicklungsaufwand als CSV

### Option D: Direkte DATEV Online-API (vollständige Integration)

**Für spätere Wachstumsphase.**

```
Eigene App
    ↓ (OAuth 2.0)
DATEV Online-API (RDS 1.0 oder BDS)
    ↓
DATEV Unternehmen online (direkt)
```

**Vorteile:**
- Vollautomatisch, keine manuellen Schritte
- Echtzeit-Datenübertragung
- Höchste professionelle Reputation

**Nachteile:**
- API-Abonnement erforderlich
- 25 Pilot-Kunden notwendig für Marktplatz-Listing
- 6–18 Monate bis zur Zertifizierung
- Asynchrone Verarbeitung komplexer als REST

---

## Empfehlung für MVP-Phasen

| Phase | Empfehlung | Zeitaufwand | Kosten |
|-------|------------|-------------|--------|
| **MVP (Monat 1–6)** | DATEV CSV-Export (Option B) | 1–2 Wochen | ~0 €/Monat |
| **Early Growth (Monat 6–18)** | lexoffice-Integration (Option A) oder DATEV XML | 4–8 Wochen | lexoffice API-Kosten |
| **Scale (ab Monat 18)** | Direkte DATEV Online-API + Marktplatz-Zertifizierung | 6–12 Monate | Entwicklung + DATEV-Gebühren |

---

## Relevanz für Produkt

### Top-3 Erkenntnisse

1. **DATEV CSV-Export ist der schnellste Einstieg**: Für den MVP (Use Case C1/C2: Belegerfassung/DATEV-Export) ist eine DATEV-CSV-Exportfunktion innerhalb von 1–2 Wochen implementierbar, kostenlos und sofort nutzbar. Kein Zertifizierungsprozess, keine 25 Pilot-Kunden notwendig. Steuerberater können CSV direkt importieren – das ist in der Praxis häufig ausreichend.

2. **lexoffice als Brücke spart 12–18 Monate Zertifizierungszeit**: Statt eine eigene DATEV-Zertifizierung anzustreben, kann man sich über die lexoffice-API in das bereits zertifizierte DATEV-Ökosystem einloggen. Das ist die smartere Startup-Strategie in der Frühphase. Viele Handwerker nutzen ohnehin bereits lexoffice (ab 5,95 €/Monat).

3. **Direkte DATEV-API ist strategisches Langzeitziel, kein MVP-Requirement**: Candis zahlt ~369 €/Monat und hat eine vollständige DATEV-Zertifizierung – ein Niveau, das für ein Startup mit Handwerker-Zielgruppe in der frühen Phase nicht erreichbar und nicht nötig ist. Der MVP braucht "gut genug": DATEV-CSV-Export + klare Anleitung für den Steuerberater.
