# Visualization Libraries

## What It Is
Demonstrating different types of plots using **matplotlib** (base plotting library) and **seaborn** (statistical visualization on top of matplotlib).

## Plots Included
1. **Line Plot** — trends over time/index
2. **Scatter Plot** — relationship between two variables
3. **Histogram** — distribution of a single variable
4. **Bar Plot** — counts of categories
5. **Box Plot** — distribution + outliers across categories
6. **Correlation Heatmap** — pairwise correlations between all numeric columns
7. **Pair Plot** — all scatter plots between numeric columns at once

## Key Concepts to Mention
- **matplotlib** is the foundation — gives full control over every element
- **seaborn** is built on matplotlib — fewer lines, better defaults, built-in statistical plots
- **Heatmap**: shows which variables are strongly correlated (positive or negative)
- **Box plot**: the box = IQR (25th-75th percentile), whiskers = 1.5×IQR, dots = outliers

## Libraries Needed
```bash
pip install pandas matplotlib seaborn
```

## How to Adapt
1. Change `FILENAME`, `NUM_COL1`, `NUM_COL2`, `CAT_COL`
2. Comment out any plot you don't need
3. For time-series data, use the date column as x-axis in line plot

## After Internet
- Install and run — plots will pop up one by one
- Sir will see actual visual output, which is the whole point of this experiment
