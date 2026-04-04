# Craftspeople AI – Projektkontext

## Vorhaben

Entwicklung einer AI-gestützten SaaS-Plattform für Handwerker.
Fokus: Büro & Verwaltung (Angebote, Kundenkommunikation, Belegerfassung).
Geschäftsmodell: Lizenz/SaaS (monatlich/jährlich).
Zielmarkt: Lokaler Markt, inhabergeführte Handwerksbetriebe 1–10 Mitarbeiter.

## Persönlicher Kontext (strategisch relevant)

- **Vater:** SHK-Betrieb (Sanitär/Heizung/Klima), kurz vor der Rente
  → Erster Referenzkunde, Interview-Partner und Betatester
- **Schwester:** Macht die Buchhaltung im väterlichen Betrieb
  → Insider-Perspektive auf Belegerfassung, DATEV, Steuerberater-Workflow
- **Ich:** IT-affin, Software-Entwickler
  → Tech-Umsetzung eigenständig möglich

## MVP Use Cases (priorisiert)

1. **A1 – AI-Angebotserstellung:** Jobbeschreibung (Text/Sprache) → fertiges PDF-Angebot
2. **B1 – Kundenkommunikation AI:** Anfragen → AI entwirft professionelle Antworten
3. **C1/C2 – Belegerfassung / DATEV-Vorbereitung:** Foto-Scan → Kategorisierung → Export

## Technischer Stack (geplant)

- AI: Claude API (Anthropic)
- Backend: Python/FastAPI + PostgreSQL
- Frontend: React
- Zahlungen: Stripe (SEPA)
- Hosting: EU-basiert (Hetzner oder AWS Frankfurt, DSGVO)

## Kritisches Risiko: DATEV

DATEV-Integration früh prüfen – Partnerprogramm oder CSV-Exportformat als Fallback.
Konkreter Testcase: Nutzt Vaters Steuerberater DATEV?

## Aktueller Stand

- [x] Projektplan & Use Cases erarbeitet (`research/plan.md`)
- [ ] Phase 1: Digitale Recherche (Wettbewerb, Marktdaten, Studien)
- [ ] Phase 2: Interview Vater + Schwester
- [ ] Phase 3: 8–12 externe Handwerker-Interviews
- [ ] MVP-Definition & Preishypothese
