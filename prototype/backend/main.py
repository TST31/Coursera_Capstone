import csv
import io
import json
import os
import re
from datetime import date, timedelta

import anthropic
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

load_dotenv()

app = FastAPI(title="Craftspeople AI – Prototyp")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class AngebotRequest(BaseModel):
    betrieb_name: str = "Mustermann SHK GmbH"
    betrieb_adresse: str = "Musterstraße 1, 12345 Musterstadt"
    betrieb_tel: str = "0123 456789"
    betrieb_email: str = "info@mustermann-shk.de"
    kunde_name: str
    kunde_adresse: str
    jobbeschreibung: str

class KommunikationRequest(BaseModel):
    betrieb_name: str = "Mustermann SHK GmbH"
    kontext: str = "SHK-Betrieb (Sanitär, Heizung, Klima)"
    kundenanfrage: str
    ton: str = "professionell-freundlich"  # professionell-freundlich | formell | locker

class BelegRequest(BaseModel):
    lieferant: str
    betrag: float
    mwst_satz: float = 19.0
    datum: str  # YYYY-MM-DD
    kategorie: str = "sonstiges"
    beschreibung: str = ""
    belegnummer: str = ""

# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def to_float(val) -> float:
    try:
        return float(str(val).replace(",", ".").replace("€", "").replace(" ", ""))
    except Exception:
        return 0.0

def extract_json(text: str) -> dict:
    """Extract JSON from Claude response even if there's surrounding text."""
    text = text.strip()
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return json.loads(text)

# ---------------------------------------------------------------------------
# Angebot HTML renderer
# ---------------------------------------------------------------------------

def render_angebot_html(req: AngebotRequest, data: dict) -> str:
    positionen_html = ""
    for pos in data.get("positionen", []):
        ep = to_float(pos.get("einzelpreis", 0))
        gp = to_float(pos.get("gesamtpreis", 0))
        positionen_html += f"""
        <tr>
          <td>{pos.get('nr', '')}</td>
          <td>{pos.get('beschreibung', '')}</td>
          <td class="r">{pos.get('menge', '')} {pos.get('einheit', '')}</td>
          <td class="r">{ep:,.2f} €</td>
          <td class="r">{gp:,.2f} €</td>
        </tr>"""

    zs = to_float(data.get("zwischensumme", 0))
    mwst = to_float(data.get("mwst_betrag", 0))
    gesamt = to_float(data.get("gesamtbetrag", 0))

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Helvetica Neue', Arial, sans-serif; color: #1f2937; background: #fff; padding: 48px; max-width: 840px; margin: 0 auto; font-size: 13px; line-height: 1.5; }}
  .header {{ display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 40px; }}
  .logo {{ font-size: 22px; font-weight: 700; color: #1d4ed8; }}
  .betrieb-info {{ font-size: 11px; color: #6b7280; margin-top: 4px; }}
  .badge {{ background: #1d4ed8; color: white; padding: 6px 18px; border-radius: 4px; font-size: 20px; font-weight: 700; letter-spacing: 2px; }}
  .meta {{ text-align: right; font-size: 12px; color: #6b7280; margin-top: 6px; }}
  .divider {{ border: none; border-top: 2px solid #1d4ed8; margin: 24px 0; }}
  .zwei-spalten {{ display: flex; justify-content: space-between; margin-bottom: 32px; }}
  .box {{ background: #f9fafb; border-radius: 6px; padding: 14px 18px; min-width: 220px; }}
  .box-label {{ font-size: 10px; text-transform: uppercase; color: #9ca3af; letter-spacing: 1px; margin-bottom: 4px; }}
  .box-content {{ font-weight: 600; }}
  table {{ width: 100%; border-collapse: collapse; margin-top: 8px; }}
  thead tr {{ background: #1d4ed8; color: white; }}
  th {{ padding: 10px 12px; text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }}
  td {{ padding: 9px 12px; border-bottom: 1px solid #f3f4f6; }}
  tr:nth-child(even) td {{ background: #f9fafb; }}
  .r {{ text-align: right; }}
  .totals {{ margin-top: 16px; display: flex; justify-content: flex-end; }}
  .totals-table {{ min-width: 280px; }}
  .totals-table td {{ border: none; padding: 4px 12px; }}
  .totals-table td:first-child {{ color: #6b7280; }}
  .totals-table td:last-child {{ text-align: right; font-weight: 500; }}
  .total-final {{ font-size: 16px; font-weight: 700; color: #1d4ed8; border-top: 2px solid #1d4ed8; }}
  .footer {{ margin-top: 48px; padding-top: 16px; border-top: 1px solid #e5e7eb; font-size: 11px; color: #9ca3af; display: flex; justify-content: space-between; }}
  .hinweis {{ background: #eff6ff; border-left: 3px solid #1d4ed8; padding: 12px 16px; margin-top: 24px; font-size: 12px; color: #1e40af; border-radius: 0 4px 4px 0; }}
</style>
</head>
<body>
  <div class="header">
    <div>
      <div class="logo">{req.betrieb_name}</div>
      <div class="betrieb-info">{req.betrieb_adresse}<br>{req.betrieb_tel} · {req.betrieb_email}</div>
    </div>
    <div>
      <div class="badge">ANGEBOT</div>
      <div class="meta">
        Nr. {data.get('angebotsnummer', 'ANB-2026-001')}<br>
        Datum: {data.get('datum', date.today().isoformat())}<br>
        Gültig bis: {data.get('gueltig_bis', '')}
      </div>
    </div>
  </div>

  <hr class="divider">

  <div class="zwei-spalten">
    <div class="box">
      <div class="box-label">Angebot für</div>
      <div class="box-content">{req.kunde_name}</div>
      <div style="color:#6b7280; font-size:12px; margin-top:4px">{req.kunde_adresse}</div>
    </div>
    <div class="box">
      <div class="box-label">Betreff</div>
      <div class="box-content">{req.jobbeschreibung[:80]}{'...' if len(req.jobbeschreibung) > 80 else ''}</div>
    </div>
  </div>

  <table>
    <thead>
      <tr>
        <th style="width:40px">Pos.</th>
        <th>Beschreibung</th>
        <th class="r" style="width:100px">Menge</th>
        <th class="r" style="width:110px">Einzelpreis</th>
        <th class="r" style="width:110px">Gesamt</th>
      </tr>
    </thead>
    <tbody>{positionen_html}</tbody>
  </table>

  <div class="totals">
    <table class="totals-table">
      <tr><td>Zwischensumme (netto)</td><td>{zs:,.2f} €</td></tr>
      <tr><td>MwSt. {data.get('mwst_satz', 19)} %</td><td>{mwst:,.2f} €</td></tr>
      <tr class="total-final"><td style="padding-top:8px">Gesamtbetrag (brutto)</td><td style="padding-top:8px">{gesamt:,.2f} €</td></tr>
    </table>
  </div>

  <div class="hinweis">
    <strong>Zahlungsbedingungen:</strong> {data.get('zahlungsbedingungen', '14 Tage netto')}<br>
    {data.get('anmerkungen', '')}
  </div>

  <div class="footer">
    <span>{req.betrieb_name} · {req.betrieb_adresse}</span>
    <span>Tel: {req.betrieb_tel} · {req.betrieb_email}</span>
  </div>
</body>
</html>"""

# ---------------------------------------------------------------------------
# API Routes
# ---------------------------------------------------------------------------

@app.post("/api/angebot")
async def create_angebot(req: AngebotRequest):
    prompt = f"""Du bist ein Assistent für einen deutschen Handwerksbetrieb.
Erstelle ein professionelles Angebot auf Basis dieser Jobbeschreibung.

Betrieb: {req.betrieb_name}
Jobbeschreibung: {req.jobbeschreibung}
Kunde: {req.kunde_name}, {req.kunde_adresse}
Datum: {date.today().isoformat()}

Antworte NUR mit einem JSON-Objekt (kein Text davor/danach):
{{
  "angebotsnummer": "ANB-{date.today().year}-001",
  "datum": "{date.today().isoformat()}",
  "gueltig_bis": "{(date.today() + timedelta(days=30)).isoformat()}",
  "positionen": [
    {{"nr": 1, "beschreibung": "...", "menge": 1.0, "einheit": "Std.", "einzelpreis": 85.00, "gesamtpreis": 85.00}}
  ],
  "zwischensumme": 0.00,
  "mwst_satz": 19,
  "mwst_betrag": 0.00,
  "gesamtbetrag": 0.00,
  "zahlungsbedingungen": "Zahlbar innerhalb von 14 Tagen ohne Abzug.",
  "anmerkungen": "..."
}}

Realistische Preise für SHK-Handwerk (Stundensatz ~85–100 €/Std. netto).
Erstelle 3–6 sinnvolle Positionen passend zur Jobbeschreibung."""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        data = extract_json(message.content[0].text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"JSON parse error: {e}\nRaw: {message.content[0].text}")

    html = render_angebot_html(req, data)
    return {"angebot": data, "html": html}


@app.post("/api/kommunikation")
async def draft_response(req: KommunikationRequest):
    ton_map = {
        "professionell-freundlich": "professionell, freundlich und verbindlich",
        "formell": "förmlich und sehr höflich",
        "locker": "locker, nahbar, trotzdem seriös",
    }
    ton_text = ton_map.get(req.ton, "professionell-freundlich")

    prompt = f"""Du bist ein Assistent für den Handwerksbetrieb "{req.betrieb_name}" ({req.kontext}).
Schreibe eine E-Mail-Antwort auf die folgende Kundenanfrage.

Ton: {ton_text}
Kundenanfrage:
---
{req.kundenanfrage}
---

Regeln:
- Sprich den Kunden mit Namen an, wenn erkennbar, sonst "Guten Tag"
- Gehe konkret auf die Anfrage ein
- Schlage einen nächsten Schritt vor (z.B. Terminvereinbarung, Rückruf)
- Maximal 120 Wörter
- Unterschrift: {req.betrieb_name}
- Kein Betreff, nur der E-Mail-Text

Antworte NUR mit dem fertigen E-Mail-Text."""

    message = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )

    return {"antwort": message.content[0].text.strip()}


@app.post("/api/datev-export")
async def datev_export(belege: list[BelegRequest]):
    if not belege:
        raise HTTPException(status_code=400, detail="Keine Belege übergeben.")

    output = io.StringIO()
    writer = csv.writer(output, delimiter=";", quoting=csv.QUOTE_MINIMAL)

    # DATEV EXTF Header (Zeile 1 + 2)
    writer.writerow([
        "EXTF", "510", "21", "Buchungsstapel", "7", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", "", "", "", "",
        date.today().strftime("%Y%m%d"), date.today().strftime("%H%M%S"),
        "", "", "", "", "", "", "", ""
    ])
    writer.writerow([
        "Umsatz (ohne Soll/Haben-Kz)", "Soll/Haben-Kennzeichen", "WKZ Umsatz",
        "Kurs", "Basis-Umsatz", "WKZ Basis-Umsatz", "Konto",
        "Gegenkonto (ohne BU-Schlüssel)", "BU-Schlüssel", "Belegdatum",
        "Belegfeld 1", "Belegfeld 2", "Skonto", "Buchungstext",
        "KOST1", "KOST2", "Beleginfo - Art 1", "Beleginfo - Inhalt 1"
    ])

    konto_map = {
        "material": "3400",
        "werkzeug": "0480",
        "fahrtkosten": "4670",
        "büro": "4930",
        "telefon": "4920",
        "bewirtung": "4650",
        "sonstiges": "4980",
    }
    bu_map = {"19.0": "9", "7.0": "8", "0.0": "40"}

    rows = []
    for beleg in belege:
        konto = konto_map.get(beleg.kategorie.lower(), "4980")
        bu = bu_map.get(str(beleg.mwst_satz), "9")
        datum_fmt = beleg.datum.replace("-", "")[6:8] + beleg.datum.replace("-", "")[4:6]  # DDMM
        belegnr = beleg.belegnummer or f"BEL-{beleg.datum.replace('-', '')}"
        text = beleg.beschreibung or beleg.lieferant

        row = [
            f"{beleg.betrag:.2f}".replace(".", ","),
            "S", "EUR", "", "", "",
            konto, "1600", bu,
            datum_fmt, belegnr, "", "",
            text[:30], "", "", "Lieferant", beleg.lieferant
        ]
        writer.writerow(row)
        rows.append({
            "lieferant": beleg.lieferant,
            "betrag": beleg.betrag,
            "konto": konto,
            "datum": beleg.datum,
            "belegnummer": belegnr,
        })

    return {"csv": output.getvalue(), "anzahl": len(belege), "vorschau": rows}


# ---------------------------------------------------------------------------
# Serve frontend
# ---------------------------------------------------------------------------

app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
