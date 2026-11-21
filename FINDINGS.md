# Nepal's Economic Evolution (2000–2025)
## Exploratory Data Analysis and Research Findings

This document presents the findings from an exploratory data analysis of Nepal's economy between 2000 and 2025.

The research aims to understand how Nepal's economy has evolved over the past 25 years, identify important economic patterns, and investigate the factors that may have influenced its performance.

The analysis uses economic indicators from the **World Bank's World Development Indicators (WDI)**, with Python for data extraction, cleaning, statistical analysis, and visualisation.

---

# 1. Data Overview

The initial analysis focuses on six economic indicators.

## 1.1 Indicator Descriptions

| Indicator | World Bank Code | Description | Unit |
|---|---|---|---|
| GDP | `NY.GDP.MKTP.KD` | Total value of goods and services produced within Nepal's economy, adjusted for price changes. | Billion constant 2015 US$ |
| GDP Growth | `NY.GDP.MKTP.KD.ZG` | Annual percentage change in real GDP, indicating the pace of economic expansion or contraction. | % |
| GDP Per Capita | `NY.GDP.PCAP.KD` | Real GDP divided by the total population, representing average economic output per person. | Constant 2015 US$ |
| GDP Per Capita Growth | `NY.GDP.PCAP.KD.ZG` | Annual percentage change in real GDP per capita. | % |
| Population Growth | `SP.POP.GROW` | Annual percentage change in the total population. | % |
| Inflation Rate | `FP.CPI.TOTL.ZG` | Annual percentage change in the Consumer Price Index (CPI), measuring changes in consumer prices. | % |

## 1.2 Important Interpretation Notes

- **Real GDP and GDP per capita:** Both are measured in constant 2015 US dollars, meaning they account for changes in prices over time.
- **GDP growth:** Measures the annual rate of expansion or contraction of the economy, not its total size.
- **GDP per capita:** Represents average economic output per person, not actual individual income or household purchasing power.
- **Population growth:** Helps explain how changes in population relate to total economic output and output per person.
- **Inflation:** Measures the annual rate of change in consumer prices, not the overall price level. A decline in inflation does not necessarily mean prices have fallen.

---

# 2. Descriptive Statistical Analysis

The dataset contains **26 annual observations**, covering 2000–2025.

The following descriptive statistics provide an overview of the distribution and variation of each indicator.

## 2.1 Descriptive Statistics Summary

| Statistic | GDP (Billion) | GDP Growth (%) | GDP Per Capita ($) | GDP PC Growth (%) | Population Growth (%) | Inflation (%) |
|---|---:|---:|---:|---:|---:|---:|
| Count | 26 | 26 | 26 | 26 | 26 | 26 |
| Mean | 23.04 | 4.19 | 826.43 | 3.38 | 0.79 | 6.15 |
| Median | 21.72 | 4.48 | 788.18 | 3.38 | 0.72 | 6.28 |
| Std. Dev. | 7.33 | 2.35 | 221.46 | 2.55 | 0.62 | 2.77 |
| Minimum | 13.43 | -2.37 | 547.22 | -4.23 | -0.15 | 2.27 |
| 25th Percentile | 16.54 | 3.44 | 621.42 | 2.50 | 0.27 | 3.30 |
| 75th Percentile | 29.58 | 5.43 | 1,029.13 | 4.51 | 1.25 | 8.68 |
| Maximum | 36.54 | 8.98 | 1,233.61 | 8.76 | 1.93 | 11.09 |

*Note: GDP is expressed in billions of constant 2015 US dollars. GDP per capita is expressed in constant 2015 US dollars. All growth rates and inflation are percentages.*

## 2.2 Individual Indicator Analysis

### A. Real GDP

| Statistic | Value |
|---|---:|
| Mean | $23.04 billion |
| Median | $21.72 billion |
| Standard deviation | $7.33 billion |
| Minimum | $13.43 billion (2000) |
| Maximum | $36.54 billion (2025) |

**Observations:**

- The mean GDP was higher than the median, indicating that the larger GDP values in the later years pulled the average upward.
- The standard deviation of $7.33 billion indicates substantial variation in GDP levels across the period.
- GDP increased from $13.43 billion in 2000 to $36.54 billion in 2025, representing approximately 2.7 times growth.

The difference between the mean and median is consistent with the long-term upward movement in GDP. However, it does not independently establish the distribution's shape.

### B. GDP Annual Growth

| Statistic | Value |
|---|---:|
| Mean | 4.19% |
| Median | 4.48% |
| Standard deviation | 2.35 percentage points |
| Minimum | -2.37% (2020) |
| Maximum | 8.98% (2017) |

**Observations:**

- Nepal recorded average annual real GDP growth of approximately 4.19%.
- The median of 4.48% was slightly higher than the mean.
- The standard deviation of 2.35 percentage points indicates noticeable variation in annual economic growth.
- The economy experienced its strongest growth in 2017 and its weakest growth in 2020.

The negative minimum indicates an actual contraction in real economic output.

### C. Real GDP Per Capita

| Statistic | Value |
|---|---:|
| Mean | $826.43 |
| Median | $788.18 |
| Standard deviation | $221.46 |
| Minimum | $547.22 (2000) |
| Maximum | $1,233.61 (2025) |

**Observations:**

- The mean was higher than the median, reflecting the increase in GDP per capita over time.
- The standard deviation of $221.46 indicates substantial variation in the levels of real GDP per capita.
- GDP per capita more than doubled between 2000 and 2025.

This indicates an increase in average real economic output per person, but it does not establish how the benefits of economic growth were distributed across the population.

### D. GDP Per Capita Growth

| Statistic | Value |
|---|---:|
| Mean | 3.38% |
| Median | 3.38% |
| Standard deviation | 2.55 percentage points |
| Minimum | -4.23% (2020) |
| Maximum | 8.76% (2017) |

**Observations:**

- Average annual GDP per capita growth was approximately 3.38%.
- The mean and median were identical when rounded to two decimal places.
- The standard deviation of 2.55 percentage points indicates considerable variation in annual per-capita growth.
- GDP per capita growth reached its highest point in 2017 and its lowest point in 2020.

The negative growth rate in 2020 indicates that average real economic output per person declined during that year.

### E. Population Growth

| Statistic | Value |
|---|---:|
| Mean | 0.79% |
| Median | 0.72% |
| Standard deviation | 0.62 percentage points |
| Minimum | -0.15% (2024) |
| Maximum | 1.93% (2020) |

**Observations:**

- Average annual population growth was approximately 0.79%.
- The mean was slightly higher than the median.
- The standard deviation of 0.62 percentage points indicates variation in population growth over the period.
- The highest recorded population growth was 1.93% in 2020.
- The minimum was -0.15% in 2024, indicating a negative estimated annual population growth rate.

The population growth figures should be interpreted alongside demographic changes, migration, and revisions to population estimates.

### F. Inflation Rate

| Statistic | Value |
|---|---:|
| Mean | 6.15% |
| Median | 6.28% |
| Standard deviation | 2.77 percentage points |
| Minimum | 2.27% (2007) |
| Maximum | 11.09% (2009) |

**Observations:**

- Average annual inflation was approximately 6.15%.
- The mean was slightly lower than the median.
- The standard deviation of 2.77 percentage points indicates noticeable variation in annual inflation rates.
- Inflation ranged from 2.27% in 2007 to 11.09% in 2009.

The relatively large range indicates that Nepal experienced substantially different rates of consumer price increases during the period.

The standard deviation measures how spread out the observations are around the mean, rather than the difference between the minimum and maximum values.

---

# 3. Economic Growth and Development

## 3.1 GDP Trend (2000–2025)

Nepal's real GDP increased from approximately $13.43 billion in 2000 to $36.54 billion in 2025.

The overall trend indicates substantial long-term economic expansion. However, economic growth was not consistent, with certain periods experiencing slower growth and contraction.

The most significant contraction occurred in 2020, when GDP growth reached -2.37%.

**Chart: Real GDP of Nepal (2000–2025)**

<img width="1000" height="500" alt="Real GDP" src="https://github.com/user-attachments/assets/3e32b15d-5d7a-48bb-9e70-b183d2dc4c6f" />


## 3.2 GDP Per Capita Trend (2000–2025)

Real GDP per capita increased from approximately $547.22 in 2000 to $1,233.61 in 2025.

This represents more than a doubling over the period.

The increase suggests that real economic output per person grew considerably over the 25 years.

However, GDP per capita does not account for income distribution and should not be treated as a direct measure of household living standards.

**Chart: Real GDP Per Capita of Nepal (2000–2025)**

<img width="1000" height="500" alt="Real GDP per Capita" src="https://github.com/user-attachments/assets/4f3d1d1e-939e-47c3-b8bc-6ead4cbf6a11" />


## 3.3 GDP and GDP Per Capita Comparison

GDP and GDP per capita followed broadly similar upward trends throughout the period.

There was no year in the dataset in which total GDP increased while GDP per capita declined.

This suggests that increases in total real economic output were accompanied by increases in average real output per person.

However, the two indicators are mathematically related because GDP per capita is calculated by dividing GDP by population. Their similar trends should therefore not be treated as independent evidence.

**Chart: GDP and GDP Per Capita Comparison (2000–2025)**

<img width="800" height="500" alt="Annual GDP and GDP Per Capita" src="https://github.com/user-attachments/assets/8eb804d1-fbae-4f6a-bede-ca4de266d20f" />


---

# 4. Population Growth and Economic Growth

## 4.1 Population Growth vs GDP Growth

A scatter plot comparing population growth and GDP growth suggested a weak negative linear relationship.

The Pearson correlation coefficient was:

- **Correlation: -0.2433**
- **Observations: 26**

This indicates that higher population growth tended to coincide with lower GDP growth in the dataset, although the relationship was weak.

Correlation does not establish causation, and other economic and demographic factors may influence both indicators.

**Chart: Population Growth vs GDP Annual Growth (2000–2025)**

<img width="800" height="500" alt="Population Growth and Real GDP growth" src="https://github.com/user-attachments/assets/79e5ef9e-981d-4aa9-bff9-28a441c8f749" />


## 4.2 Population Growth vs GDP Per Capita Growth

Population growth and GDP per capita growth are also important to examine together.

GDP per capita growth reflects how quickly average real output per person changes. Population growth provides important demographic context for interpreting this indicator.

**Chart: Population Growth vs GDP Per Capita Growth (2000–2025)**

<img width="800" height="500" alt="Population Growth and GDP per capita growth" src="https://github.com/user-attachments/assets/7c9e94e2-142e-4bab-adad-34f934fea488" />


*The final statistical interpretation of this relationship remains pending.*

---

# 5. Inflation and Economic Performance

## 5.1 Inflation Trend (2000–2025)

The inflation chart revealed several notable patterns:

1. **Considerable fluctuations:** Inflation varied substantially throughout the period, indicating that the rate of increase in consumer prices was not particularly stable.
2. **Declining trend after 2009:** Following its peak in 2009, inflation generally followed a downward trend, although there were periods of renewed increases.
3. **Sharp decline in 2017:** A particularly noticeable decline occurred between 2016 and 2017.
4. **Repeated fluctuations:** Inflation appeared to follow a recurring pattern of increasing for a few years, declining for a few years, and subsequently increasing again.

These are observations from the time-series chart. They do not establish a regular economic cycle.

**Chart: Inflation Rate of Nepal (2000–2025)**

<img width="1000" height="500" alt="Inflation" src="https://github.com/user-attachments/assets/0ca80d0d-3869-41cc-b0b9-3d0b69e7181d" />


## 5.2 Inflation vs GDP Growth

The Pearson correlation coefficient between inflation and GDP growth was:

- **Correlation: -0.0753**
- **Observations: 26**

The coefficient is very close to zero, indicating almost no linear association between the two variables across the full period.

**Chart: Inflation vs GDP Annual Growth (2000–2025)**

<img width="800" height="500" alt="Inflation and Real GDP Growth" src="https://github.com/user-attachments/assets/beeb53fb-6c5e-41fd-9991-0ea3c1ec21f7" />


## 5.3 Inflation vs GDP Per Capita Growth

The Pearson correlation coefficient between inflation and GDP per capita growth was:

- **Correlation: 0.0181**
- **Observations: 26**

This also indicates almost no linear association between the two variables.

**Chart: Inflation vs GDP Per Capita Growth (2000–2025)**

<img width="800" height="500" alt="Inflation and Real GDP per capita Growth" src="https://github.com/user-attachments/assets/661ddb57-de86-46f0-b9ed-f045388d62ab" />


### Interpretation

The initial statistical analysis does not indicate a meaningful linear relationship between inflation and either GDP growth or GDP per capita growth.

However, this does not mean inflation has no influence on economic activity. Its effects may depend on the source of inflation, the economic environment, and the time period being examined.

---

# 6. Important Economic Periods and Historical Explanations

This section connects notable changes in the statistical data with historical and economic developments in Nepal.

The explanations below represent potential contributing factors identified during historical research. Their individual contributions have not been established through causal analysis.

## 6.1 2002–2003: Economic Slowdown and Recovery

| Year | GDP Growth |
|---|---:|
| 2002 | 0.12% |
| 2003 | 3.95% |

GDP growth reached an exceptionally low level in 2002 before recovering in 2003.

Potential contributing factors:

- **Civil conflict:** Nepal's Maoist insurgency intensified, creating uncertainty and disrupting economic activities.
- **State of Emergency:** Security measures and instability affected economic confidence and business activity.
- **Tourism disruption:** Political instability and security concerns affected Nepal's tourism industry.
- **Weak agricultural performance:** Poor monsoon conditions may have contributed to lower agricultural output.

The subsequent improvement in 2003 suggests a recovery from the exceptionally weak performance of the previous year.

## 6.2 2007: Lowest Inflation

<badge color="success">2.27% inflation</badge>

Nepal recorded its lowest annual inflation rate in the dataset in 2007.

Potential contributing factors:

- **Currency appreciation:** The Nepalese rupee, pegged to the Indian rupee, benefited from the Indian rupee's appreciation against the US dollar. This may have reduced the cost of imports priced in foreign currencies.
- **Favourable fuel base effect:** Earlier petroleum price increases dropped out of the annual comparison, potentially easing transport and non-food inflation.
- **Post-war supply normalization:** The November 2006 Comprehensive Peace Accord helped bring an end to the armed conflict, potentially reducing highway blockades, checkpoints, and other supply disruptions.
- **Monetary and fiscal conditions:** Relatively restrained monetary and fiscal conditions may have limited inflationary pressure.

These factors provide possible explanations for the low inflation rate, but their individual effects require supporting evidence.

## 6.3 2009: Highest Inflation

<badge color="warning">11.09% inflation</badge>

Inflation reached its highest level in the dataset in 2009.

Potential contributing factors:

- **Food supply shocks:** Weak monsoon conditions and drought in Nepal and India affected agricultural production. Food supply disruptions and restrictions on some Indian food exports may have increased domestic food prices.
- **Currency depreciation:** Depreciation of the Nepalese rupee against the US dollar increased the cost of imported goods and commodities.
- **Global oil price transmission:** The sharp rise in international oil prices during 2008 and subsequent domestic fuel price adjustments may have contributed to higher transportation and production costs.
- **Remittance and liquidity growth:** Strong remittance inflows and expansion in the money supply may have increased domestic demand, adding to inflationary pressure.
- **Government expenditure and wage increases:** Expansionary government spending and increases in wages may have contributed to demand and production costs.
- **Load-shedding and strikes:** Frequent electricity shortages forced businesses to rely on expensive alternatives such as diesel generators. Strikes and supply-chain disruptions may also have increased production and distribution costs.

The combination of food, fuel, currency, and domestic demand pressures provides several possible explanations for the exceptionally high inflation rate.

## 6.4 2017: Strongest Economic Growth and Low Inflation

<badge color="success">8.98% GDP growth</badge> <badge color="success">2.78% inflation</badge>

2017 was a particularly interesting year because Nepal recorded its highest GDP growth rate in the dataset while inflation was relatively low.

Potential contributing factors:

- **Post-blockade recovery:** Normalization of trade following the 2015–2016 border blockade helped restore imports, supply chains, and economic activity.
- **Agricultural performance:** A favourable monsoon and strong agricultural harvest contributed to higher agricultural output and increased food availability.
- **End of load-shedding:** Improvements in electricity supply reduced the reliance of businesses on expensive diesel generators, potentially lowering production costs.
- **Reconstruction activity:** Reconstruction following the 2015 earthquake contributed to economic activity and investment.
- **Indian inflation conditions:** Relatively low inflation in India may have helped limit imported inflation in Nepal.
- **Credit conditions:** Nepal Rastra Bank's tighter credit policies may have helped moderate speculative lending and domestic demand pressures.

The combination of economic recovery, agricultural output, improved electricity supply, and reconstruction activity may help explain the strong economic performance in 2017.

## 6.5 2018–2019: Moderation in Economic Growth

| Year | GDP Growth |
|---|---:|
| 2018 | 7.62% |
| 2019 | 6.66% |

Following the exceptionally strong growth recorded in 2017, economic growth moderated in the subsequent years.

Potential contributing factors:

- **Fading base effect:** Some of the unusually strong growth in 2017 reflected the recovery from earlier disruptions.
- **Bank liquidity constraints:** Liquidity pressures in the banking sector may have constrained credit availability.
- **Slower migration:** Changes in foreign employment and migration patterns may have influenced remittance inflows and domestic economic activity.
- **Federalism implementation:** Administrative restructuring and implementation challenges may have affected public spending and project execution.

Despite the moderation, GDP growth remained relatively strong in both years.


## 6.6 2020: Economic Contraction

<badge color="danger">-2.37% GDP growth</badge>

Nepal recorded its lowest GDP growth rate in the dataset in 2020. GDP per capita growth also reached its lowest point at -4.23%.

Potential contributing factors:

- **COVID-19 lockdowns:** Restrictions on movement and business operations disrupted economic activity.
- **Border closures:** Restrictions on cross-border movement and trade affected supply chains and domestic commerce.
- **Tourism collapse:** International travel restrictions severely affected tourism-related businesses.
- **Construction slowdown:** Project delays, labour shortages, and restrictions on economic activity affected construction.
- **Employment disruption:** Many workers experienced reduced employment opportunities and income.

The contraction in 2020 represents a major disruption in Nepal's long-term economic growth trajectory.


---

# 7. Summary of Important Years

| Year | Indicator | Finding |
|---|---|---|
| 2000 | GDP | Lowest recorded value: $13.43 billion |
| 2000 | GDP per capita | Lowest recorded value: $547.22 |
| 2002 | GDP growth | Exceptionally low growth: 0.12% |
| 2007 | Inflation | Lowest recorded inflation: 2.27% |
| 2009 | Inflation | Highest recorded inflation: 11.09% |
| 2017 | GDP growth | Highest recorded growth: 8.98% |
| 2017 | GDP per capita growth | Highest recorded growth: 8.76% |
| 2017 | Inflation | Relatively low inflation: approximately 2.78% |
| 2020 | GDP growth | Lowest recorded growth: -2.37% |
| 2020 | GDP per capita growth | Lowest recorded growth: -4.23% |
| 2020 | Population growth | Highest recorded growth: 1.93% |
| 2025 | GDP | Highest recorded value: $36.54 billion |
| 2025 | GDP per capita | Highest recorded value: $1,233.61 |

## 7.1 Major Changes Between Selected Years

| Period | Indicator | Change |
|---|---|---|
| 2000–2025 | GDP | Increased from $13.43B to $36.54B |
| 2000–2025 | GDP per capita | Increased from $547.22 to $1,233.61 |
| 2007–2009 | Inflation | Increased from 2.27% to 11.09% |
| 2016–2017 | GDP growth | Reached its period maximum of 8.98% in 2017 |
| 2016–2017 | GDP per capita growth | Reached its period maximum of 8.76% in 2017 |
| 2019–2020 | GDP growth | Fell to -2.37% |
| 2019–2020 | GDP per capita growth | Fell to -4.23% |

*Note: This table highlights selected major changes, not every annual increase or decrease.*

---

# 8. Methodological Considerations

The following principles guide the research:

- **Correlation is not causation:** Correlation coefficients describe statistical associations, not causal relationships.
- **Preserve valid observations:** Unusual observations should be investigated rather than automatically removed.
- **Consider sample size:** The dataset contains only 26 annual observations, so statistical conclusions must be interpreted cautiously.
- **Distinguish real and nominal values:** GDP and GDP per capita are measured in constant 2015 US dollars.
- **Interpret GDP per capita carefully:** It measures average output per person, not actual individual income or income distribution.
- **Interpret inflation carefully:** CPI inflation measures the annual percentage change in consumer prices, not the overall price level.
- **Separate observations from explanations:** Statistical patterns are identified through EDA, while historical explanations require independent supporting evidence.

---



---

# 9. Sources and References

The primary statistical source for this project is:

- [World Bank — World Development Indicators](https://databank.worldbank.org/source/world-development-indicators)

Historical explanations should be supported with additional sources, particularly:

- Nepal Rastra Bank publications and annual reports.
- Government of Nepal economic surveys.
- World Bank economic updates and reports.
- Asian Development Bank reports.
- International Monetary Fund publications.
- Relevant historical and economic research papers.

**Research note:** Historical explanations in this document are currently documented as potential contributing factors. Specific claims, numerical estimates, and causal interpretations must be verified and cited before the findings are considered final.
