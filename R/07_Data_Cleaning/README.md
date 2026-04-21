# Data Cleaning + Visualization — R

## What It Is
Clean raw data and then visualize it. Auto-detects numeric and categorical columns.

## Cleaning Steps
1. Check missing values (`is.na`)
2. Fill with median (numeric) / mode (categorical)
3. Remove duplicates (`unique`)
4. Print summary statistics

## Libraries Needed
```r
install.packages("ggplot2")
```

## How to Adapt
Just change `FILENAME` — everything else is auto-detected.

## After Internet
Install ggplot2 and run. Plots auto-adapt to your data.

## Tip
R's `summary()` gives a quick statistical overview — mean, median, quartiles. Mention this when showing to sir.
