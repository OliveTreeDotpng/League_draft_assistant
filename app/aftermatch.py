import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from datetime import datetime, UTC
from src.data.db import init_db, save_feedback

st.title("Efter matchen")
init_db()

col1, col2 = st.columns(2)
with col1:
    outcome = st.radio("Vann ni", ["Ja", "Nej"])
    chosen = st.text_input("Vilken champion spelade du", "Ahri")
    notes = st.text_area("Kommentar", "")
with col2:
    patch = st.text_input("Patch", "14.15")
    tier = st.selectbox("Rank", ["Iron","Bronze","Silver","Gold","Platinum","Emerald","Diamond","Master+"])

if st.button("Spara"):
    row = {
        "timestamp": datetime.now(UTC).isoformat(),
        "patch": patch, "tier": tier,
        "ally_top": "", "ally_jungle": "", "ally_mid": "", "ally_adc": "", "ally_support": "",
        "enemy_top": "", "enemy_jungle": "", "enemy_mid": "", "enemy_adc": "", "enemy_support": "",
        "your_role": "", "recommended_pick": "", "chosen_pick": chosen,
        "predicted_win_prob": None,
        "outcome_win": 1 if outcome == "Ja" else 0,
        "notes": notes
    }
    save_feedback(row)
    st.success("Sparat")
