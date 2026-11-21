"""
Indicator Extraction
--------------------
Extracts selected macroeconomic indicators for Nepal (2000-2025) from a
World Bank-style CSV, reshapes each one into a long (Year, value) table,
merges them all on 'Year', and exports a single master dataset.

Only pandas and the Python standard library are used.
"""

from functools import reduce
from pathlib import Path

import pandas as pd


# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

INPUT_FILE = BASE_DIR / "NepalData.csv"
OUTPUT_FILE = BASE_DIR / "Master Data.csv"

SKIP_ROWS = 4

START_YEAR = 2000
END_YEAR = 2025
YEARS = [str(year) for year in range(START_YEAR, END_YEAR + 1)]

BILLION = 1_000_000_000

# (Indicator Code, output column name, divisor, decimals to round to)
# The order here is the column order of the final merged dataset.
INDICATORS = [
    ("NY.GDP.MKTP.KD",       "Annual GDP (Billion)",                    BILLION, 3),
    ("NY.GDP.MKTP.KD.ZG",    "GDP Annual Growth",                       1,       2),
    ("NY.GDP.PCAP.KD",       "GDP Per Capita",                          1,       2),
    ("NY.GDP.PCAP.KD.ZG",    "Annual GDP_PC Growth",                    1,       2),
    ("FP.CPI.TOTL.ZG",       "Inflation Rate",                          1,       2),
    ("BX.TRF.PWKR.DT.GD.ZS", "Remittance (% of GDP)",                   1,       2),
    ("NE.EXP.GNFS.ZS",       "Export (% of GDP)",                       1,       2),
    ("NE.IMP.GNFS.ZS",       "Import (% of GDP)",                       1,       2),
    ("NE.GDI.TOTL.ZS",       "Gross Capital (% of GDP)",                1,       2),
    ("SP.POP.GROW",          "Population Growth (annual %)",            1,       2),
    ("SL.UEM.TOTL.ZS",       "Unemployment Rate (annual %)",            1,       2),
    ("BX.KLT.DINV.WD.GD.ZS", "FDI (% of GDP)",                          1,       2),
    ("NE.CON.PRVT.KD",       "Annual Household Consumption (Billion)",  BILLION, 3),
    ("NE.CON.PRVT.PC.KD.ZG", "Consumption growth",                      1,       2),
]


# --------------------------------------------------------------------------
# Functions
# --------------------------------------------------------------------------
def load_data(path: Path) -> pd.DataFrame:
    """Load the raw CSV and keep only the id columns plus the 2000-2025 years."""
    raw = pd.read_csv(path, skiprows=SKIP_ROWS)
    id_columns = ["Country Name", "Country Code", "Indicator Name", "Indicator Code"]
    return raw[id_columns + YEARS]


def extract_indicator(
    data: pd.DataFrame,
    code: str,
    column_name: str,
    divisor: float = 1,
    decimals: int = 2,
) -> pd.DataFrame:
    """Pull one indicator's row and reshape it into a long (Year, value) table."""
    rows = data[data["Indicator Code"] == code]
    if rows.empty:
        raise ValueError(f"Indicator code '{code}' not found in the dataset.")

    long_table = pd.melt(
        rows,
        value_vars=YEARS,
        var_name="Year",
        value_name=column_name,
    )
    long_table[column_name] = (long_table[column_name] / divisor).round(decimals)
    return long_table


def build_master_data(data: pd.DataFrame) -> pd.DataFrame:
    """Extract every configured indicator and merge them all on 'Year'."""
    tables = [
        extract_indicator(data, code, name, divisor, decimals)
        for code, name, divisor, decimals in INDICATORS
    ]
    return reduce(
        lambda left, right: pd.merge(left, right, on="Year", how="outer"),
        tables,
    )


def check_data(master: pd.DataFrame) -> None:
    """Print quick quality checks on the merged dataset."""
    print(f"Shape: {master.shape}")
    print(f"Total cells: {master.size}")
    print(f"Duplicate years: {master.duplicated('Year').sum()}")
    print("\nMissing values per column:")
    print(master.isna().sum())
    print("\nData types:")
    print(master.dtypes)
    print("\nFirst 5 rows:")
    print(master.head())


def main() -> None:
    data = load_data(INPUT_FILE)
    master_data = build_master_data(data)
    check_data(master_data)

    master_data.to_csv(OUTPUT_FILE, index=False)
    print(f"\nMaster dataset exported to '{OUTPUT_FILE}'.")


if __name__ == "__main__":
    main()
