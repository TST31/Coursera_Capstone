#!/bin/bash
set -e

cd "$(dirname "$0")/backend"

if [ ! -f .env ]; then
  echo "⚠️  Keine .env gefunden. Kopiere .env.example und trage deinen API-Key ein:"
  echo "    cp .env.example .env && nano .env"
  exit 1
fi

if [ ! -d venv ]; then
  echo "🔧 Erstelle virtuelle Umgebung..."
  python3 -m venv venv
fi

source venv/bin/activate
pip install -q -r requirements.txt

echo ""
echo "✅ Craftspeople AI Prototyp startet..."
echo "   → http://localhost:8000"
echo ""
uvicorn main:app --reload --port 8000
