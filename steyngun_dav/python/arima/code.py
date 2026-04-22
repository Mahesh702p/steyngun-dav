# # Time Series Analysis using ARIMA
# # ARIMA(p, d, q) — AutoRegressive Integrated Moving Average

# import pandas as pd
# from statsmodels.tsa.arima.model import ARIMA
# from sklearn.metrics import mean_squared_error
# import math

# # ============ CHANGE THESE ============
# FILENAME = "data.csv"
# DATE_COL = "Date"       # date/time column
# VALUE_COL = "Value"     # the value to forecast
# ORDER = (1, 1, 1)       # (p, d, q) — start with (1,1,1), tune if needed
# # ======================================

# # --- Load ---
# df = pd.read_csv(FILENAME, parse_dates=[DATE_COL])
# df = df.sort_values(DATE_COL)
# df.set_index(DATE_COL, inplace=True)
# print("Shape:", df.shape)
# print(df.head())

# series = df[VALUE_COL]

# # --- Train/Test Split (last 20% for testing) ---
# split = int(len(series) * 0.8)
# train, test = series[:split], series[split:]
# print(f"\nTrain: {len(train)}, Test: {len(test)}")

# # --- Fit ARIMA ---
# model = ARIMA(train, order=ORDER)
# fitted = model.fit()
# print(fitted.summary())

# # --- Forecast ---
# forecast = fitted.forecast(steps=len(test))

# # --- Evaluate ---
# rmse = math.sqrt(mean_squared_error(test, forecast))
# print(f"\nRMSE: {rmse:.4f}")

# # --- Show predictions ---
# print("\n--- First 5 Actual vs Forecast ---")
# for i in range(min(5, len(test))):
#     print(f"Actual: {test.iloc[i]:.2f}  Forecast: {forecast.iloc[i]:.2f}")


import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("data.csv", parse_dates=["Date"])
df.set_index("Date", inplace=True)

model = ARIMA(df["Value"], order=(1,1,1)).fit()
forecast = model.forecast(steps=20)
print(forecast)

import matplotlib.pyplot as plt
df["Value"].plot(label="Actual")
forecast.plot(label="Forecast", color="red")
plt.legend()
plt.savefig("arima_result.png")