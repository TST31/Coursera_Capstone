# Craftspeople AI – Research & Execution Plan

## Projektkontext

**Ziel:** AI-SaaS für Handwerker bauen, Fokus auf Büro & Verwaltung (Angebote, Rechnungen, Kundenkommunikation).

**Persönlicher Kontext (wichtig für Strategie):**
- Vater: SHK-Betrieb (Sanitär/Heizung/Klima), kurz vor der Rente
- Schwester: macht die Buchhaltung im väterlichen Betrieb
- Ich: IT-affin, Software-Entwickler

→ Das ist kein zufälliger Markt. Du hast direkten Zugang zu einem echten Betrieb,
  der als Referenzkunde, Interview-Partner und Betatester dienen kann.

---

## Überblick: Was ist digital vs. persönlich machbar?

| Typ | Aktivität | Medium |
|---|---|---|
| Digital | Marktdaten (HWK, Destatis) | Online |
| Digital | Studien zu Digitalisierung im Handwerk | Online |
| Digital | Wettbewerbs-Analyse (Preise, Features) | Online |
| Digital | App-Store-Reviews analysieren | Online |
| Digital | Google Maps Betriebe erfassen | Online |
| Digital | Google-Bewertungen auswerten | Online |
| Digital | Branchenportale & Foren lesen | Online |
| Persönlich | Interview mit Vater + Schwester | Vor Ort |
| Persönlich | Weitere Handwerker-Interviews | Telefon/vor Ort |
| Persönlich | Innung / HWK kontaktieren | Telefon/E-Mail |

---

## Phase 1: Digitale Recherche (alles remote, sofort startbar)

### 1.1 Marktgröße & Struktur

**Quellen:**
- [HWK der jeweiligen Kammer](https://www.hwk.de) → Betriebsstatistik für die Region
- [Destatis](https://www.destatis.de) → Handwerkszählung, Betriebsgrößen
- [IfM Bonn](https://www.ifm-bonn.org) → KMU-Daten, speziell Handwerk
- [ZDH Statistisches Taschenbuch](https://www.zdh.de) → Gewerkeverteilung, Umsätze

**Zieldaten:**
- Anzahl SHK-Betriebe in Deutschland und Anteil an Gesamthandwerk
- Durchschnittliche Betriebsgröße (Mitarbeiter)
- Altersstruktur der Betriebsinhaber (ZDH veröffentlicht das)
- Anteil Solo-Selbstständige vs. 2–10 Mitarbeiter

### 1.2 Digitalisierungsstudien

Folgende Studien auswerten:

- **ZDH "Digitalisierung im Handwerk"** – aktuellste Ausgabe
- **Bitkom KMU-Studie** – Cloud, AI, Software-Adoption
- **BMWK Mittelstandsbericht** – Digitalisierungsstand KMU
- **Fraunhofer IAO** – Digitale Transformation Handwerk

**Gesuchte Erkenntnisse:**
- Welche Software nutzen Handwerker heute schon?
- Wie viele Stunden/Woche verbringen sie mit Admin?
- Was verhindert Technologie-Adoption? (Komplexität? Preis? Vertrauen?)
- Zahlungsbereitschaft für Digitalisierungstools?

### 1.3 Wettbewerbs-Analyse

Für jeden Wettbewerber erfassen: Preis, Kernfeatures, App-Store-Rating, häufigste Kritik-Punkte.

**Direkte Wettbewerber (Handwerk-spezifisch):**
- Meister (meister.de)
- Craftboxx
- Tailor (tailor-crm.de)
- MeinBüro Handwerk
- Dispatcher Phönix
- Pave (pave.de)

**Indirekte Wettbewerber (allg. Bürosoftware):**
- sevDesk
- lexoffice (Lexware)
- FastBill
- Billomat

**Für Belegerfassung / DATEV speziell:**
- Dext (früher Receipt Bank)
- Candis
- DATEV Unternehmen Online
- GetMyInvoices

**Pro Wettbewerber analysieren:**
1. Preisseite: Was kostet welches Paket?
2. Google Play / App Store: Bewertungen (besonders 2–3 Sterne = echte Pain Points)
3. Trustpilot / Capterra: Nutzer-Kritik
4. Landing Page: Welche Hauptversprechen machen sie?
5. Haben sie AI-Features? Wenn ja welche?

**Erkenntnisziel:** Wo sind die Lücken? Was sagen Handwerker, was ihnen fehlt?

### 1.4 Google Maps Analyse der Zielregion

**Ziel:** Überblick über alle Handwerker-Betriebe in der Zielstadt/dem Zielkreis.

**Methode:**
- Google Maps Suche: "Sanitär [Stadt]", "Elektriker [Stadt]", "Maler [Stadt]" etc.
- Für jeden Betrieb notieren:
  - Anzahl Bewertungen (→ Proxy für Betriebsgröße / Aktivität)
  - Bewertungs-Durchschnitt
  - Hat Betrieb eine Website? (ja/nein)
  - Reagiert Inhaber auf Google-Bewertungen? (→ Proxy für Tech-Affinität)
  - Öffnungszeiten vollständig gepflegt?

**Tool-Option:** Outscraper (outscraper.com) kann Google Maps-Daten strukturiert exportieren.

### 1.5 Branchenforen & Communities lesen

Passiv lesen, nicht aktiv posten:

- **Facebook-Gruppen:** "Handwerker Deutschland", "SHK Meister Forum"
- **Reddit:** r/Handwerk
- **Xing-Gruppen:** Handwerk & Mittelstand
- **Branchenmagazine:** SBZ (Sanitär, Heizung, Klima), IKZ, Elektro+

**Was suchen:** Wiederkehrende Fragen, Beschwerden, Empfehlungen – echte Pain Points.

---

## Phase 2: Interne Interviews (Vater + Schwester)

Das ist der unfaire Vorteil: Direkter Zugang zu einem echten SHK-Betrieb.

### Interview mit Vater (Betriebsinhaber)

**Fokus:** Betriebsalltag, Kundenkontakt, Angebots-/Rechnungsprozess

Fragen:
- Wie läuft es ab, wenn ein Neukunde anruft bis zur ersten Rechnung?
- Wie lange dauert ein Angebot schreiben? Was ist das Nervigste daran?
- Welche Software nutzt du? Wofür? Was nervt dich daran?
- Was würdest du sofort auslagern, wenn es jemand für dich erledigen würde?
- Wie viele Stunden Bürokram pro Woche ungefähr?

### Interview mit Schwester (Buchhaltung)

**Fokus:** Buchführung, Belege, Rechnungen, Jahresabschluss-Vorbereitung

Fragen:
- Was sind die größten manuellen Aufwände in der Buchhaltung?
- Wie kommen Rechnungen rein / raus? Alles digital oder noch Papier?
- Was macht ihr schon digital? Was würdest du gerne automatisieren?
- Habt ihr DATEV? Wie läuft der Steuerberater-Prozess?
- Was würde euch am meisten Zeit sparen?

**Ziel:** Echten Workflow dokumentieren, als Referenzprozess für MVP nutzen.

---

## Phase 3: Externe Interviews (8–12 Betriebe)

Erst nach Phase 1 & 2, damit man mit Wissen reingeht.

**Gesprächspartner gewinnen:**
1. Warm-Intro durch Vater ("Kennst du noch SHK-Kollegen?")
2. Lokale Innung kontaktieren (E-Mail genügt als Einstieg)
3. Direktansprache: "Ich entwickle Software für Handwerker und würde gern 20 Minuten von Ihrem Alltag lernen"

**Interview-Leitfaden (Kernfragen):**
- Erzähl mir von einem typischen Tag – was nervt dich am meisten?
- Wie erstellst du Angebote und Rechnungen? Wie lange dauert das?
- Welche Software nutzt du? Was fehlt dir?
- Wärst du bereit, 30–50 €/Monat für ein Tool zu zahlen, das dir 3 Stunden/Woche spart?

---

## Use Cases – Priorisierte Liste

### MVP-Kern

| # | Use Case | Beschreibung | Zeiteinsparung |
|---|---|---|---|
| A1 | **AI-Angebotserstellung** | Jobbeschreibung (Text/Sprache) → fertiges PDF-Angebot | 20–40 min → 3 min |
| B1 | **Kundenkommunikation AI** | Kundenanfrage → AI entwirft professionelle Antwort | 5–10 min → 1 min |
| C1/C2 | **Belegerfassung / DATEV** | Foto von Beleg → Kategorisierung → DATEV-Export | Stunden/Monat → Minuten |

### Folgefeatures

| # | Use Case | Beschreibung |
|---|---|---|
| A2 | Angebot zu Rechnung | 1-Klick-Umwandlung nach Auftragsabschluss |
| A4/C4 | Nachfassen & Mahnwesen | Offene Angebote und Rechnungen automatisch nachfassen |
| D1 | Monteur-Briefings | AI generiert Einsatzdokument für Mitarbeiter |
| B3/B4 | Bewertungsmanagement | Antworten auf Google-Reviews, automatische Bewertungsanfragen |

### Alle Use Cases (Langfristig)

**Zone A – Angebot/Rechnung:** A1 AI-Angebote, A2 Angebot→Rechnung, A3 Materialkalkulation, A4 Nachverfolgung

**Zone B – Kundenkommunikation:** B1 Anfragen beantworten, B2 Terminbestätigung, B3 Bewertungsantworten, B4 Bewertungsanfragen

**Zone C – Büro/Buchhaltung:** C1 Belegscan, C2 DATEV-Export, C3 Monatsübersicht, C4 Mahnwesen

**Zone D – Betrieb:** D1 Monteur-Briefings, D2 Terminplanung, D3 Gewährleistungs-Tracking

**Zone E – Neukundengewinnung:** E1 Website-Texte, E2 Social Media, E3 Google Ads

---

## Technischer Risiko-Check: DATEV

DATEV ist in Deutschland tief verwurzelt, aber mit geschlossenen Schnittstellen.

**Optionen:**
- DATEV-Marktplatz-Partnerprogramm (API-Zugang, aber bürokratisch)
- DATEV-Exportformate (CSV) – ohne Partnerschaft implementierbar
- Konkreter Testcase: Nutzt Vaters Steuerberater DATEV?

---

## Wettbewerbs-Recherche: Suchqueries je Use Case

### A1 – AI-Angebotserstellung
- "AI Angebotserstellung Handwerk"
- "KI Handwerkersoftware Angebot"
- "Handwerker App Angebot erstellen Test 2025"

### B1 – AI Kundenkommunikation
- "Handwerker Kundenanfragen automatisch beantworten"
- "WhatsApp Handwerk CRM Integration"
- "AI E-Mail-Assistent Handwerker"

### C1/C2 – Belegerfassung & DATEV
- "Belegerfassung Handwerk DATEV Integration Vergleich"
- "Candis vs Dext DATEV"
- "Handwerker Buchhaltung Software Test 2025"

---

## Deliverables

- [ ] Markt-Übersicht: Betriebsanzahl, Gewerkeverteilung, Altersstruktur
- [ ] Wettbewerbs-Matrix: Preise, Features, AI-Stand, Schwachstellen
- [ ] Interview-Dokument: Vater + Schwester (Referenzkunde)
- [ ] 8–12 externe Interview-Zusammenfassungen
- [ ] Persona: Zielkunde (Gewerk, Alter, Größe, Schmerzpunkt)
- [ ] MVP-Feature-Liste (priorisiert)
- [ ] Preishypothese mit Begründung

---

## Technischer Ausblick (nach Research)

- AI-Core: Claude API (Anthropic) – stark in strukturiertem Textoutput
- Stack: Python/FastAPI + PostgreSQL + React
- Zahlungen: Stripe (SEPA für DE)
- Hosting: EU-basiert (Hetzner oder AWS Frankfurt, DSGVO-konform)
