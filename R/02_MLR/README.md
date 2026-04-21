# Multiple Linear Regression — R

## What It Is
Uses R's built-in `lm()` function to fit a model with multiple predictors. `target ~ .` means "predict target using all other columns."

## Key Concepts
- `lm()` is R's linear model function — base R, no install needed
- `summary(model)` shows coefficients, p-values, R-squared, F-statistic
- **p-value < 0.05** means the predictor is statistically significant
- `***` next to a predictor = very significant

## Libraries Needed
**NONE** — `lm()` and `predict()` are base R.

## How to Adapt
1. Change `FILENAME` and `TARGET`
2. If you want specific predictors (not all columns): `model <- lm(target ~ col1 + col2, data = train)`

## After Internet
```r
plot(y_actual, y_pred, main="Actual vs Predicted", pch=19)
abline(0, 1, col="red", lwd=2)
```
