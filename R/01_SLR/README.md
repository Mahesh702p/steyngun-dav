# Simple Linear Regression (From Scratch) — R

## What It Is
Same as Python version: fits `y = mx + c` using pure math. No `lm()` function used.

## Key Concepts
- Same formulas as Python: m = Σ((xi-x̄)(yi-ȳ)) / Σ((xi-x̄)²)
- R has built-in `mean()`, `sum()` — those are allowed (basic math, not ML)
- `read.csv()` is base R — no package needed

## Libraries Needed
**NONE** — pure base R.

## How to Adapt
1. Change `FILENAME`, `X_COL`, `Y_COL`
2. Run in RStudio or `Rscript code.R`

## After Internet
- Add a plot:
```r
plot(X, Y, main="SLR", xlab=X_COL, ylab=Y_COL, pch=19)
abline(c, m, col="red", lwd=2)
legend("topleft", legend="Regression Line", col="red", lwd=2)
```
