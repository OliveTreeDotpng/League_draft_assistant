from dotenv import load_dotenv
import os

# Ladda .env-filen
load_dotenv()

RIOT_API_KEY = os.getenv("RIOT_API_KEY")

if not RIOT_API_KEY:
    raise ValueError("Ingen Riot API-nyckel hittades. Lägg till RIOT_API_KEY i .env")

# Exempel: använd nyckeln i en request
import requests

def get_account_by_riot_id(game_name, tag_line, region="europe"):
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
    headers = {"X-Riot-Token": RIOT_API_KEY}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()
