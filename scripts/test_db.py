import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from datetime import datetime
from src.data.db import init_db, save_feedback, fetch_feedback

init_db()
row = {
    "timestamp": datetime.utcnow().isoformat(),
    "patch": "14.15",
    "tier": "Gold",
    "ally_top": "Garen", "ally_jungle": "Vi", "ally_mid": "Ahri", "ally_adc": "Jinx", "ally_support": "Leona",
    "enemy_top": "Darius", "enemy_jungle": "LeeSin", "enemy_mid": "Orianna", "enemy_adc": "Ezreal", "enemy_support": "Nami",
    "your_role": "Mid", "recommended_pick": "Ahri", "chosen_pick": "Ahri",
    "predicted_win_prob": 0.62, "outcome_win": 1, "notes": "Stark engage och bra pick"
}
save_feedback(row)
print(fetch_feedback(1))