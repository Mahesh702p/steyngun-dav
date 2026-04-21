# Visualization Libraries — R

## What It Is
Demonstrates **ggplot2** (tidyverse plotting) and base R plots.

## Plots Included
1. Scatter, 2. Histogram, 3. Bar, 4. Box, 5. Line, 6. Density, 7. Correlation Heatmap

## Key Concepts
- `ggplot2` uses **grammar of graphics**: data + aesthetics + geometries
- `aes()` maps data to visual properties, `geom_*()` draws the shapes
- `theme_minimal()` gives a clean look
- Base R `heatmap()` used for correlation matrix

## Libraries Needed
```r
install.packages("ggplot2")
```

## How to Adapt
Change `FILENAME`, `NUM_COL1`, `NUM_COL2`, `CAT_COL`.

## Tip
ggplot2 is the gold standard in R visualization. If sir asks R vs Python for viz: "R's ggplot2 is more powerful for statistical plots, Python's matplotlib gives more low-level control."
