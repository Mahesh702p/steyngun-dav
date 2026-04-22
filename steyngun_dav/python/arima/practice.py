from statsmodels.tsa.arima.model import ARIMA
import pandas as pd

df = pd.read_csv("data.csv", parse_dates = ["Date"])
df.set_index("Date", inplace = True)

model = ARIMA(df["Value"], order = (1,1,1)).fit()
forecast = model.forecast(steps = 12)

print(forecast)
