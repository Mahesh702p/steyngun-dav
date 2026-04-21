import pandas as pd
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

# Load data
df = pd.read_csv("data.csv")
X = df[['X']]
y = df['Y']

# Split data (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit model on training data
model = LinearRegression().fit(X_train, y_train)

# Print results
print(f"m: {model.coef_[0]}")
print(f"c: {model.intercept_}")
print(f"R2 (Test Data): {model.score(X_test, y_test)}")
