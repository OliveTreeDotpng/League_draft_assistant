from pathlib import Path
from typing import Optional, List, Tuple
import pandas as pd # type: ignore

DATA_PATH = Path("data/processed/matches_processed.parquet")  # byt till din fil om du vill

REQUIRED_COLS = [
    "match_id","patch","queue","tier",
    "ally_top","ally_jungle","ally_mid","ally_adc","ally_support",
    "enemy_top","enemy_jungle","enemy_mid","enemy_adc","enemy_support",
    "win"
]

def load_matches(path: Optional[Path] = None) -> pd.DataFrame:
    """Läs in datasetet, parq om möjligt, annars csv. Säkerställ nödvändiga kolumner finns."""
    p = Path(path) if path else DATA_PATH
    if p.suffix.lower() == ".parquet":
        df = pd.read_parquet(p)
    else:
        df = pd.read_csv(p)
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Saknar kolumner, {missing}")
    return df

def apply_filters(
    df: pd.DataFrame,
    patches: Optional[List[str]] = None,
    tiers: Optional[List[str]] = None,
    queues: Optional[List[str]] = None,
    team_side: str = "both"  # "blue", "red", "both"
) -> pd.DataFrame:
    """Applicera enkla filter på patch, tier, queue, team side. Returnerar filtrerad df."""
    out = df.copy()
    if patches:
        out = out[out["patch"].astype(str).isin(patches)]
    if tiers:
        out = out[out["tier"].astype(str).isin(tiers)]
    if queues:
        out = out[out["queue"].astype(str).isin(queues)]
    # Team side kan användas senare när du separerar blå mot röd
    return out

def winrate_summary(df: pd.DataFrame) -> Tuple[int, float]:
    """Returnerar antal matcher och total winrate i procent."""
    n = len(df)
    if n == 0:
        return 0, 0.0
    wr = 100.0 * df["win"].mean()
    return n, wr

def winrate_by_role(df: pd.DataFrame, role: str) -> pd.DataFrame:
    """Beräkna winrate per champion för en vald roll, sorterad efter winrate, visa även count."""
    col = f"ally_{role.lower()}"  # exempel, ally_mid
    sub = df[[col, "win"]].rename(columns={col: "champ"})
    grp = sub.groupby("champ").agg(matches=("win","size"), winrate=("win","mean")).reset_index()
    grp["winrate"] = grp["winrate"] * 100.0
    grp = grp.sort_values(["matches","winrate"], ascending=[False, False])
    return grp
