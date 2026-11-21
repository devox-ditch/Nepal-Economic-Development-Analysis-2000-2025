# Nepal's Economic Evolution (2000–2025)

An exploratory data analysis project investigating how Nepal's economy has evolved between 2000 and 2025 and the factors associated with its economic performance.

## Research Question

**How has Nepal's economy evolved between 2000 and 2025, and what factors have influenced its economic performance?**

This project uses annual economic indicators from the World Bank's World Development Indicators (WDI) database. Through data extraction, cleaning, exploratory data analysis, visualisation, and historical research, the project aims to identify long-term trends, important economic periods, and relationships between indicators.

## Research Themes

The project is organised into six themes:

1. **Economic Growth and Development** – GDP, GDP per capita, economic growth, population growth, and inflation.
2. **Remittances and Foreign Employment** – the role of remittance flows in Nepal's economy.
3. **Inflation and Purchasing Power** – changes in consumer prices and their implications for purchasing power.
4. **International Trade: Imports and Exports** – Nepal's trade patterns and external dependence.
5. **Employment and Population** – labour-market indicators and demographic changes.
6. **Comparing Nepal with Neighbouring Economies** – placing Nepal's economic performance in a regional context.

The analysis is exploratory. Relationships between indicators are treated as associations unless additional evidence supports a causal explanation.

## Data Source

- **Source:** [World Bank – World Development Indicators](https://databank.worldbank.org/source/world-development-indicators)
- **Country:** Nepal (`NPL`)
- **Period:** 2000–2025
- **Frequency:** Annual
- **Original dataset:** `NepalData.csv`

### Main Indicators

| Indicator                                      | WDI Code               | Unit              |
| ---------------------------------------------- | ---------------------- | ----------------- |
| GDP per capita (constant 2015 US$)             | `NY.GDP.PCAP.KD`       | Constant 2015 US$ |
| GDP growth (annual %)                          | `NY.GDP.MKTP.KD.ZG`    | %                 |
| Inflation, consumer prices (annual %)          | `FP.CPI.TOTL.ZG`       | %                 |
| Personal remittances received (% GDP)          | `BX.TRF.PWKR.DT.GD.ZS` | % of GDP          |
| Exports of goods and services (% GDP)          | `NE.EXP.GNFS.ZS`       | % of GDP          |
| Imports of goods and services (% GDP)          | `NE.IMP.GNFS.ZS`       | % of GDP          |
| Gross capital formation (% GDP)                | `NE.GDI.TOTL.ZS`       | % of GDP          |
| Population growth (annual %)                   | `SP.POP.GROW`          | %                 |
| Unemployment, total (ILO modelled estimate)    | `SL.UEM.TOTL.ZS`       | % of labour force |
| Foreign direct investment, net inflows (% GDP) | `BX.KLT.DINV.WD.GD.ZS` | % of GDP          |

Additional indicators are included in the wider master dataset for future analysis, including private consumption growth, total GDP, GDP per capita growth, and household consumption.

## Project Workflow

The project follows a structured data analysis workflow:

1. **Data Extraction** – retrieve and select Nepal's WDI records for 2000–2025.
2. **Indicator Extraction** – extract relevant indicators using their WDI codes and reshape annual data into a structured format.
3. **Master Dataset Construction** – combine the selected indicators into one dataset using the year as the common key.
4. **Data Cleaning** – select the variables required for each research theme, check data types, missing values, and duplicate observations.
5. **Exploratory Data Analysis** – examine descriptive statistics, visualise trends, investigate relationships, and identify unusual periods.
6. **Historical Research** – investigate possible explanations for observed economic developments using credible sources.

## Current Analysis: Economic Growth and Development

The current working dataset includes:

- Annual GDP (constant 2015 US$, billions)
- GDP annual growth
- GDP per capita (constant 2015 US$)
- GDP per capita growth
- Population growth
- Inflation rate

The broader master dataset is retained for the remaining research themes.

## Tools and Libraries

- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook

## Current Progress

- [x] Downloaded and inspected World Bank WDI data.
- [x] Extracted annual data for 2000–2025.
- [x] Selected and extracted the required economic indicators.
- [x] Constructed the master dataset.
- [x] Completed initial data-quality checks.
- [x] Started exploratory analysis of economic growth and development.
- [x] Examined GDP and GDP per capita trends.
- [x] Investigated the relationship between population growth and GDP growth.
- [x] Complete the inflation analysis for Theme 1.
- [ ] Complete the remaining research themes.
- [ ] Investigate historical explanations for major economic developments.
- [ ] Complete the comparison with neighbouring economies.

## Methodological Considerations

- GDP and GDP per capita are measured in constant 2015 US dollars, representing real rather than current-price values.
- GDP per capita represents average economic output per person, not actual individual income.
- CPI inflation measures the annual rate of change in consumer prices, not the price level itself.
- Correlation indicates association, not causation.
- The dataset contains only 26 annual observations, so statistical results require cautious interpretation.
- Unusual observations should be investigated rather than automatically removed.
- Historical explanations and causal claims require supporting evidence beyond the observed data.

## Findings

The detailed research findings, interpretations, statistical results, and pending investigations are documented separately in [**FINDINGS.md**](FINDINGS.md).
