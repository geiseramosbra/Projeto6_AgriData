
import pandas as pd
from pathlib import Path

def find_input_file(base: Path) -> Path:
    """Return path to real (raw) WB CSV if present; else fallback to synthetic."""
    raw = base / "data" / "raw" / "worldbank_indicators_latam.csv"
    if raw.exists():
        return raw
    return base / "data" / "synthetic" / "agridata_latam_synthetic.csv"
