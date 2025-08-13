import sqlite3
from pathlib import Path
from typing import Dict, Any

# Ange var SQLite-databasen ska ligga
DB_PATH = Path("db/lol_feedback.db")

# SQL-schema för feedback-tabellen
SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- unikt ID för varje rad
    timestamp TEXT,                         -- tidpunkt när feedbacken sparades
    patch TEXT,                             -- LoL patch-version
    tier TEXT,                              -- spelarens rank
    ally_top TEXT, ally_jungle TEXT, ally_mid TEXT, ally_adc TEXT, ally_support TEXT, -- allierade picks
    enemy_top TEXT, enemy_jungle TEXT, enemy_mid TEXT, enemy_adc TEXT, enemy_support TEXT, -- motståndares picks
    your_role TEXT,                         -- spelarens roll
    recommended_pick TEXT,                  -- vad modellen rekommenderade
    chosen_pick TEXT,                        -- vad spelaren valde
    predicted_win_prob REAL,                 -- modellens predikterade vinstsannolikhet
    outcome_win INTEGER,                     -- matchens utfall (1=vinst, 0=förlust)
    notes TEXT                               -- extra kommentarer
);
"""

def get_conn():
    """Skapar en databasanslutning och ser till att mappen finns."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)  # skapa db/-mappen om den inte finns
    con = sqlite3.connect(DB_PATH)  # anslut till databasen
    return con # Detta returnerar en anslutning som kan användas för att köra SQL-frågor

def init_db():
    """Initierar databasen med rätt schema om det inte redan finns."""
    with get_conn() as con:
        con.executescript(SCHEMA_SQL)

def save_feedback(row: Dict[str, Any]):
    """Sparar en feedback-post i databasen."""
    cols = ",".join(row.keys())
    qs = ",".join(["?"] * len(row))  # placeholders för värden
    with get_conn() as con:
        con.execute(f"INSERT INTO feedback ({cols}) VALUES ({qs})", list(row.values()))

def fetch_feedback(limit: int = 20):
    """Hämtar de senaste feedback-posterna, standard max 20 st."""
    with get_conn() as con:
        cur = con.execute("SELECT * FROM feedback ORDER BY id DESC LIMIT ?", (limit,))
        cols = [c[0] for c in cur.description]  # kolumnnamn från tabellen
        return [dict(zip(cols, r)) for r in cur.fetchall()]
