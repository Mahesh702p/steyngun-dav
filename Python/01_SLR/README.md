# Simple Linear Regression (From Scratch)

## What It Is
Fits a straight line `y = mx + c` through data points to predict a continuous target variable from one independent variable. **No libraries used** — pure math only.

## Key Concepts to Mention to Sir
- **m (slope)** = Σ((xi - x̄)(yi - ȳ)) / Σ((xi - x̄)²) — measures change in Y per unit change in X
- **c (intercept)** = ȳ - m * x̄ — the Y value when X = 0
- **R-squared** — proportion of variance in Y explained by X (closer to 1 = better)
- **RMSE** — average prediction error (lower = better)

## Libraries Needed
**NONE** — only `csv` (built-in) and `math` (built-in) are used.

## How to Adapt to Any Dataset
1. Place your CSV file in the same folder
2. Change `FILENAME` to your CSV filename
3. Change `X_COL` to the name of the independent variable column
4. Change `Y_COL` to the name of the dependent variable column

## After Internet is Given
- You can add a matplotlib scatter plot to visually show the regression line:
```python
import matplotlib.pyplot as plt
plt.scatter(X, Y, color='blue', label='Actual')
plt.plot(X, Y_pred, color='red', label='Regression Line')
plt.xlabel(X_COL)
plt.ylabel(Y_COL)
plt.legend()
plt.title('Simple Linear Regression')
plt.show()
```
- This makes a much stronger impression when showing to sir

## Tip
If sir asks "why no library?", say: "To understand the underlying mathematics — how slope and intercept are derived from the least squares method."
