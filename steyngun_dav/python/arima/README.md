# Time Series Analysis using ARIMA

## What It Is
ARIMA (AutoRegressive Integrated Moving Average) is used to forecast future values from a time-ordered sequence (stock prices, temperature, sales, etc.).

## Key Concepts to Mention
- **AR (p)**: uses past values (lags) to predict future — autoregression
- **I (d)**: differencing to make data stationary (removes trends)
- **MA (q)**: uses past forecast errors
- **Stationarity**: ARIMA needs stationary data — constant mean and variance over time
- Common starting order: **(1,1,1)** — works as a reasonable baseline
- **AIC/BIC** in summary: lower = better model

## Libraries Needed
```bash
pip install pandas statsmodels scikit-learn
```

## How to Adapt
1. Change `FILENAME`, `DATE_COL`, `VALUE_COL`
2. Data must have a date/time column and a numeric value column
3. Tune `ORDER = (p, d, q)` if RMSE is too high. Try (2,1,2) or (1,1,0)

## After Internet
- Install dependencies and run
- Add a forecast plot:
```python
import matplotlib.pyplot as plt
plt.plot(train.index, train, label='Train')
plt.plot(test.index, test, label='Actual')
plt.plot(test.index, forecast, label='Forecast', linestyle='--')
plt.legend(); plt.title('ARIMA Forecast'); plt.show()
```

## Tip
If sir asks about choosing p, d, q: "I used (1,1,1) as a baseline. Ideally we use ACF and PACF plots — ACF for q, PACF for p, and d is the number of differences needed for stationarity."
