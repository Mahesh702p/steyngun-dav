# Time Series ARIMA — R

## What It Is
Uses `auto.arima()` from the `forecast` package — automatically selects the best (p, d, q) based on AIC.

## Key Concepts
- `auto.arima()` tries multiple combinations and picks the best
- `ts()` creates a time series object; `frequency` = 12 for monthly, 4 for quarterly
- `forecast()` generates future predictions with confidence intervals

## Libraries Needed
```r
install.packages("forecast")
```

## How to Adapt
1. Change `FILENAME`, `DATE_COL`, `VALUE_COL`
2. Change `frequency` in `ts()` based on your data interval

## After Internet
```r
plot(fc, main="ARIMA Forecast")
lines(ts(actual, start=end(train)+1, frequency=12), col="red")
legend("topleft", legend=c("Forecast", "Actual"), col=c("blue","red"), lwd=2)
```

## Tip
R advantage: `auto.arima()` auto-selects best order — in Python you'd have to manually try different orders or use `pmdarima`.
