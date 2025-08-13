# app/EDA.py

# Gör src hittbar när Streamlit kör filen direkt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st # type: ignore
import pandas as pd
import plotly.express as px # type: ignore
from src.data.loader import load_matches, apply_filters, winrate_summary, winrate_by_role

st.set_page_config(page_title="EDA", layout="wide")
st.title("EDA, utforska datasetet")

# Sidopanel, filter
with st.sidebar:
    st.header("Filter")
    data_path = st.text_input("Sökväg till data", "data/processed/matches_processed.parquet")
    patches = st.text_input("Patch, kommaseparerat", "14.15")
    tiers = st.multiselect("Rank", ["Iron","Bronze","Silver","Gold","Platinum","Emerald","Diamond","Master+"], default=["Gold","Platinum","Emerald"])
    queues = st.multiselect("Queue", ["ranked_solo","ranked_flex"], default=["ranked_solo"])
    role = st.selectbox("Roll för winrate per champion", ["top","jungle","mid","adc","support"], index=2)
    min_matches = st.slider("Min antal matcher per champion", 20, 500, 50, step=10)

# Läs data
try:
    df = load_matches(Path(data_path))
except Exception as e:
    st.error(f"Kunde inte läsa data, {e}")
    st.stop()

# Applicera filter
f_patches = [p.strip() for p in patches.split(",")] if patches.strip() else None
df_filt = apply_filters(df, patches=f_patches, tiers=tiers, queues=queues)

# Översikt
n, wr = winrate_summary(df_filt) # n = matcher, wr = winrate procent
st.subheader("Översikt")
st.write({"matcher": n, "total winrate procent": round(wr, 2)})

if n == 0:
    st.warning("Inget data efter filter, justera filtren ovan")
    st.stop()

# Graf, winrate per champion inom vald roll
st.subheader(f"Winrate per champion, roll, {role}")
tbl = winrate_by_role(df_filt, role)
tbl = tbl[tbl["matches"] >= min_matches]

left, right = st.columns([2,1])
with left:
    fig = px.bar(tbl.head(30), x="champ", y="winrate", hover_data=["matches"])
    fig.update_layout(xaxis_title="Champion", yaxis_title="Winrate procent")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.caption("Topp 10 som tabell")
    st.dataframe(tbl.head(10), use_container_width=True)

# Exportknapp för nuvarande filter
st.download_button(
    label="Exportera filtrerad data till CSV",
    data=df_filt.to_csv(index=False),
    file_name="filtered_matches.csv",
    mime="text/csv",
)
