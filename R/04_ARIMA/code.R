# Time Series Analysis using ARIMA in R
# Uses the forecast package

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
DATE_COL <- "Date"
VALUE_COL <- "Value"
# ======================================

library(forecast)

# --- Load ---
df <- read.csv(FILENAME)
df[[DATE_COL]] <- as.Date(df[[DATE_COL]])
df <- df[order(df[[DATE_COL]]), ]
cat("Loaded", nrow(df), "rows\n")

series <- ts(df[[VALUE_COL]], frequency = 12)  # frequency: 12=monthly, 4=quarterly, 1=yearly

# --- Train/Test Split ---
split <- floor(length(series) * 0.8)
train <- window(series, end = c(1, split))
test_len <- length(series) - split

# --- Auto ARIMA (automatically picks best p, d, q) ---
model <- auto.arima(train)
print(summary(model))

# --- Forecast ---
fc <- forecast(model, h = test_len)
print(fc)

# --- RMSE ---
actual <- tail(df[[VALUE_COL]], test_len)
predicted <- as.numeric(fc$mean)
rmse <- sqrt(mean((actual - predicted)^2))
cat("\nRMSE:", round(rmse, 4), "\n")

# --- First 5 ---
cat("\n--- First 5 Actual vs Forecast ---\n")
for (i in 1:min(5, test_len)) {
  cat("Actual:", round(actual[i], 2), " Forecast:", round(predicted[i], 2), "\n")
}

# --- CLEAN & PERFECT ARIMA ---
# library(forecast)
# df <- read.csv("data.csv")
# model <- auto.arima(ts(df$Value))
# plot(forecast(model, h=5))
