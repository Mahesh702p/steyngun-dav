# Multiple Linear Regression

## What It Is
Extends SLR to multiple independent variables: `y = b0 + b1*x1 + b2*x2 + ...`. Used when the target depends on more than one feature.

## Key Concepts to Mention
- **Each coefficient** tells how much Y changes when that X changes by 1 unit (other Xs held constant)
- **R-squared** still indicates model fit quality
- **Train-test split** prevents overfitting — we evaluate on unseen data
- Difference from SLR: multiple features, same least squares idea

## Libraries Needed
```bash
pip install pandas scikit-learn
```

## How to Adapt
1. Change `FILENAME` to your CSV
2. Change `X_COLS` to a list of your feature column names
3. Change `Y_COL` to your target column name

## After Internet
- Install dependencies, run the code, show the coefficients and R-squared
- Optional: add a visualization of actual vs predicted:
```python
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()
```
