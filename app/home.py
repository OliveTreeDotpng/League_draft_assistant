import streamlit as st # type: ignore
from pathlib import Path

st.set_page_config(page_title="LoL Draft Assistant", layout="wide")

st.title("LoL Draft Assistant")
st.caption("Projektpitch, databeskrivning, och snabbstart")

st.markdown("""
**Mål**, visa hela ML processen, EDA, modell, utvärdering och ett driftläge i Streamlit.
**Data**, matcher med picks och win, kolumner som match_id, patch, tier, ally och enemy per roll, samt win som mål.
""")

# Liten sanity check så användaren ser att filstruktur stämmer
exists_parquet = Path("data/processed/matches_processed.parquet").exists()
exists_csv = Path("data/raw/matches_raw.csv").exists()

st.write("Kontroll, finns datafilerna")
st.write({
    "processed_parquet": exists_parquet,
    "raw_csv": exists_csv
})

st.info("Gå vidare till EDA sidan när du har en första datafil på plats")
