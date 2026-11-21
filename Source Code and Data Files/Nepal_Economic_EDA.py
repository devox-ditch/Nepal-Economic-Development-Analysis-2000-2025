"""
NEPAL: EXPLORATORY DATA ANALYSIS (2000–2025)
============================================

Purpose
-------
Prepare and explore the core indicators needed to investigate Nepal's
economic growth and development.

Indicators retained in the analysis DataFrame
---------------------------------------------
1. Real GDP (constant 2015 US$, expressed in billions)
2. Real GDP growth (annual %)
3. Real GDP per capita (constant 2015 US$)
4. Real GDP per capita growth (annual %)
5. Population growth (annual %)
6. Inflation rate (consumer prices, annual %)

Input
-----
Master Data.csv

The input CSV is expected to contain the columns listed in REQUIRED_COLUMNS.
GDP growth and GDP per capita growth are expected to already be present in
the master dataset. This script does not recalculate them.

Notes
-----
- GDP and GDP per capita are real measures, adjusted for price changes.
- Inflation is the annual percentage change in consumer prices.
- Correlation describes association; it does not establish causation.
- Do not remove unusual years from the main analysis simply because they
appear unusual. Investigate them and report sensitivity checks separately.
"""

# =============================================================================
# 1. IMPORTS AND CONFIGURATION
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

DATA_FILE = "Master Data.csv"
START_YEAR = 2000
END_YEAR = 2025

# Keep the analysis focused on the indicators required for this investigation.
REQUIRED_COLUMNS = [
    "Year",
    "Annual GDP (Billion)",
    "GDP Annual Growth",
    "GDP Per Capita",
    "Annual GDP_PC Growth",
    "Population Growth (annual %)",
    "Inflation Rate",
]


# =============================================================================
# 2. LOAD AND PREPARE THE DATA
# =============================================================================

# Load the master dataset.
master_df = pd.read_csv(DATA_FILE)

# Check that every required indicator is available before selecting columns.
missing_columns = [
    column for column in REQUIRED_COLUMNS
    if column not in master_df.columns
]

if missing_columns:
    raise ValueError(
        "The input file is missing required columns: "
        + ", ".join(missing_columns)
    )

# Create a focused DataFrame containing only the indicators used in this EDA.
df = master_df[REQUIRED_COLUMNS].copy()

# Ensure years are numeric, then retain the study period and sort chronologically.
df["Year"] = pd.to_numeric(df["Year"], errors="raise").astype(int)
df = (
    df.loc[df["Year"].between(START_YEAR, END_YEAR)].sort_values("Year").reset_index(drop=True)
)

# Confirm the expected period and check for missing values.
expected_years = set(range(START_YEAR, END_YEAR + 1))
available_years = set(df["Year"])

if available_years != expected_years:
    missing_years = sorted(expected_years - available_years)
    raise ValueError(f"Missing years in the study period: {missing_years}")

if df[REQUIRED_COLUMNS[1:]].isna().any().any():
    missing_data = df[REQUIRED_COLUMNS].isna().sum()
    raise ValueError(
        "Missing values detected. Review these column counts:\n"
        + missing_data[missing_data > 0].to_string()
    )

# Display a quick overview of the prepared dataset.
print("Dataset dimensions:", df.shape)
print("\nColumns included:")
print(df.columns.tolist())
print("\nFirst five observations:")
print(df.head())


# =============================================================================
# 3. DESCRIPTIVE STATISTICS
# =============================================================================

# Summarise the distribution of each numerical indicator.
print("\nDescriptive statistics:")
print(df.drop(columns="Year").describe().round(2))

# Identify the years with the lowest and highest values for selected indicators.
# These are useful starting points for investigating notable periods.
indicators_to_check = [
    "Annual GDP (Billion)",
    "GDP Annual Growth",
    "GDP Per Capita",
    "Annual GDP_PC Growth",
    "Population Growth (annual %)",
    "Inflation Rate",
]

print("\nMinimum and maximum values by indicator:")
for indicator in indicators_to_check:
    min_row = df.loc[df[indicator].idxmin(), ["Year", indicator]]
    max_row = df.loc[df[indicator].idxmax(), ["Year", indicator]]

    print(
        f"{indicator}: "
        f"minimum = {min_row[indicator]:.2f} ({int(min_row['Year'])}), "
        f"maximum = {max_row[indicator]:.2f} ({int(max_row['Year'])})"
    )


# =============================================================================
# 4. TRENDS OVER TIME
# =============================================================================

def plot_time_series(column, title, y_label):
    
    ax = df.plot(
        x="Year",
        y=column,
        kind="line",
        figsize=(10, 5),
        marker="o",
        legend=False,
        title=title,
    )
    ax.set_xlabel("Year")
    ax.set_ylabel(y_label)
    ax.grid(axis="both", alpha=0.3)
    plt.tight_layout()
    plt.show()


# GDP level and growth
plot_time_series(
    "Annual GDP (Billion)",
    "Nepal: Real GDP (2000–2025)",
    "Real GDP (billion, constant 2015 US$)",
)

plot_time_series(
    "GDP Annual Growth",
    "Nepal: Real GDP Growth (2000–2025)",
    "Annual GDP growth (%)",
)

# GDP per capita level and growth
plot_time_series(
    "GDP Per Capita",
    "Nepal: Real GDP per Capita (2000–2025)",
    "Real GDP per capita (constant 2015 US$)",
)

plot_time_series(
    "Annual GDP_PC Growth",
    "Nepal: Real GDP per Capita Growth (2000–2025)",
    "Annual GDP per capita growth (%)",
)

# Population growth and inflation
plot_time_series(
    "Population Growth (annual %)",
    "Nepal: Population Growth (2000–2025)",
    "Population growth (%)",
)

plot_time_series(
    "Inflation Rate",
    "Nepal: Annual Consumer Price Inflation (2000–2025)",
    "Inflation rate (%)",
)


# =============================================================================
# 5. COMPARING ANNUAL GROWTH RATES
# =============================================================================

# Compare GDP growth, GDP per capita growth, and population growth.
# This helps show how total output growth relates to growth per person.
plt.figure(figsize=(10, 5))

plt.plot(
    df["Year"],
    df["GDP Annual Growth"],
    marker="o",
    linewidth=2,
    label="Real GDP growth (%)",
)

plt.plot(
    df["Year"],
    df["Annual GDP_PC Growth"],
    marker="o",
    linewidth=2,
    label="Real GDP per capita growth (%)",
)

plt.plot(
    df["Year"],
    df["Population Growth (annual %)"],
    linestyle="--",
    linewidth=1.8,
    label="Population growth (%)",
)

plt.axhline(0, color="grey", linestyle=":", linewidth=0.8)
plt.title("Nepal: GDP, GDP per Capita, and Population Growth (2000–2025)")
plt.xlabel("Year")
plt.ylabel("Annual growth (%)")
plt.grid(axis="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 5))

plt.plot(
    df["Year"],
    df["Inflation Rate"],
    marker="o",
    linewidth=2,
    label="Inflation Rate (%)",
)

plt.plot(
    df["Year"],
    df["GDP Annual Growth"],
    marker="o",
    linewidth=2,
    label="Real GDP growth (%)",
)


plt.axhline(0, color="grey", linestyle=":", linewidth=0.8)
plt.title("Nepal: GDP, GDP per Capita, and Population Growth (2000–2025)")
plt.xlabel("Year")
plt.ylabel("Annual growth (%)")
plt.grid(axis="both", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
# =============================================================================
# 6. EXPLORING RELATIONSHIPS
# =============================================================================

def plot_relationship(x_column, y_column, title, x_label, y_label):
    """Create a scatter plot to inspect the relationship between two indicators."""
    #plot_df = df[df[x_column]>0]
    #log_x = n(plot_df[x_column])
    plt.figure(figsize=(8, 5))
    plt.scatter(df[x_column], df[y_column], alpha=0.8)
    #plt.plot(df[x_column], df[y_column], alpha=0.8)
    plt.title(title)
    #plt.xlabel(log_x)
    plt.xlabel(x_column)
    plt.ylabel(y_label)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()

plot_relationship(
    "Inflation Rate",
    "GDP Annual Growth",
    "Inflation and Real GDP Growth (2000–2025)",
    "Inflation rate (%)",
    "Real GDP growth (%)",
)


# Annual GDP and GDP Per Capita. line and scatter plot 
plot_relationship(
    "Annual GDP (Billion)",
    "GDP Per Capita",
    "Annual GDP and GDP Per Capita (2000–2025)",
    "Annual GDP ($Billion)",
    "GDP Per Capita ($)",
)

# GDP growth and GDP Per Capita Growth.
plot_relationship(
    "GDP Annual Growth",
    "Annual GDP_PC Growth",
    "Annual GDP Growth and GDP Per Capita Growth(2000–2025)",
    "Annual GDP Growth (%)",
    "GDP Per Capita Growth (%)",
)



# Population growth compared with the pace of economic growth.
plot_relationship(
    "Population Growth (annual %)",
    "GDP Annual Growth",
    "Population Growth and Real GDP Growth (2000–2025)",
    "Population growth (%)",
    "Real GDP growth (%)",
)

# Population growth compared with the pace of economic growth per capita.
plot_relationship(
    "Population Growth (annual %)",
    "Annual GDP_PC Growth",
    "Population Growth and GDP Per Capita Growth (2000–2025)",
    "Population growth (%)",
    "Annual GDP Per Capita growth (%)",
)

# Inflation compared with the pace of economic growth.
plot_relationship(
    "Inflation Rate",
    "GDP Annual Growth",
    "Inflation and Real GDP Growth (2000–2025)",
    "Inflation rate (%)",
    "Real GDP growth (%)",
)

# Inflation compared with growth in real output per person.
plot_relationship(
    "Inflation Rate",
    "Annual GDP_PC Growth",
    "Inflation and Real GDP per Capita Growth (2000–2025)",
    "Inflation rate (%)",
    "Real GDP per capita growth (%)",
)


# =============================================================================
# 7. PEARSON CORRELATIONS
# =============================================================================

# Use growth rates rather than GDP levels for the main inflation comparisons.
# GDP levels tend to trend over time, which can produce misleading correlations.
correlation_pairs = {
    "Inflation vs. GDP growth": ("Inflation Rate", "GDP Annual Growth"),
    "Inflation vs. GDP per capita growth": (
        "Inflation Rate",
        "Annual GDP_PC Growth",
    ),
    "Population growth vs. GDP growth": (
        "Population Growth (annual %)",
        "GDP Annual Growth",
    ),
}


print("\nPearson correlation coefficients:")
for label, (x_column, y_column) in correlation_pairs.items():
    coefficient = df[x_column].corr(df[y_column])
    print(f"{label}: {coefficient:.4f}")

# Interpret these coefficients alongside the plots and historical context.
# A correlation coefficient alone cannot explain why a relationship exists.
