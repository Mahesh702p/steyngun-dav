# Simple Linear Regression - FROM SCRATCH (No sklearn)
# Uses pandas/numpy for data handling, but regression math is manual
# Formula: y = mx + c
# m = Σ((xi - x̄)(yi - ȳ)) / Σ((xi - x̄)²)
# c = ȳ - m * x̄

import pandas as pd
import numpy as np

# ============ CHANGE THESE ============
FILENAME = "data.csv"
X_COL = "X"   # column name for independent variable
Y_COL = "Y"   # column name for dependent variable
# ======================================

# --- Read CSV ---
df = pd.read_csv(FILENAME)
X = df[X_COL].values
Y = df[Y_COL].values
n = len(X)
print(f"Loaded {n} data points")
print(df.head())

# --- Calculate Means ---
x_mean = np.mean(X)
y_mean = np.mean(Y)
print(f"\nMean of X: {x_mean:.4f}")
print(f"Mean of Y: {y_mean:.4f}")

# --- Calculate m (slope) and c (intercept) ---
numerator = np.sum((X - x_mean) * (Y - y_mean))
denominator = np.sum((X - x_mean) ** 2)

m = numerator / denominator
c = y_mean - m * x_mean
print(f"\nRegression Equation: y = {m:.4f} * x + {c:.4f}")

# --- Predictions ---
Y_pred = m * X + c

# --- R-squared ---
ss_res = np.sum((Y - Y_pred) ** 2)
ss_tot = np.sum((Y - y_mean) ** 2)
r_squared = 1 - (ss_res / ss_tot)
print(f"R-squared: {r_squared:.4f}")

# --- RMSE ---
rmse = np.sqrt(ss_res / n)
print(f"RMSE: {rmse:.4f}")

# --- Predict for a new value ---
x_new = float(input("\nEnter a value of X to predict Y: "))
y_new = m * x_new + c
print(f"Predicted Y for X={x_new}: {y_new:.4f}")

# --- Print first few predictions ---
print("\n--- First 5 Actual vs Predicted ---")
for i in range(min(5, n)):
    print(f"X={X[i]:.2f}  Actual Y={Y[i]:.2f}  Predicted Y={Y_pred[i]:.2f}")
