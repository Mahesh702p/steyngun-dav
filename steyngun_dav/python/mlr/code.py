# Multiple Linear Regression using sklearn
# y = b0 + b1*x1 + b2*x2 + ... + bn*xn

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# ============ CHANGE THESE ============
FILENAME = "data.csv"
X_COLS = ["col1", "col2", "col3"]  # independent variable columns
Y_COL = "target"                    # dependent variable column
# ======================================

# --- Load Data ---
df = pd.read_csv(FILENAME)

X = df[X_COLS]
y = df[Y_COL]

# --- Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTrain: {len(X_train)}, Test: {len(X_test)}")

# --- Train ---
model = LinearRegression()
model.fit(X_train, y_train)
# --- Evaluation & Results ---
y_pred = model.predict(X_test)

print("\n--- MODEL PERFORMANCE ---")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficients: {dict(zip(X_COLS, model.coef_.round(2)))}") # Names & Values in 1 line
print(f"R-squared: {r2_score(y_test, y_pred):.2f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")

# Optional: Ultra-short comparison
print("\nActual vs Predicted (Test Set):")
print(pd.DataFrame({'Actual': y_test, 'Predicted': y_pred}).head())

print(dir(model))

dir(model)
