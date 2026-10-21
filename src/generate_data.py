# Synthetic-data generator pattern.
# The repository includes a ready-to-use 10,000-row CSV.
# Change SEED / distributions below to create alternate scenarios.
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
ROWS = 10_000

print("This repository ships with data/procurement_data.csv.")
print("See the notebook and README for the full data-generation methodology.")
print(f"Configured seed={SEED}, rows={ROWS:,}.")
