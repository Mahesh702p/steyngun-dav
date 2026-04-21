# Logistic Regression

## What It Is
A **classification** algorithm (not regression despite the name). Predicts probability of a binary outcome (0 or 1) using the sigmoid function. Used for yes/no problems like spam detection, disease prediction, etc.

## Key Concepts to Mention
- **Sigmoid function**: maps any value to 0-1 range → interpreted as probability
- **Confusion Matrix**: shows TP, TN, FP, FN → helps evaluate classifier
- **Accuracy, Precision, Recall, F1-score**: key classification metrics
- Unlike linear regression, output is a **class label** not a continuous value
- Uses **log-loss** (cross-entropy) as the cost function, not MSE

## Libraries Needed
```bash
pip install pandas scikit-learn
```

## How to Adapt
1. Change `FILENAME`, `X_COLS`, `Y_COL`
2. Make sure `Y_COL` contains binary values (0/1)
3. If your target has text labels like "Yes"/"No", encode them first:
   ```python
   df[Y_COL] = df[Y_COL].map({"Yes": 1, "No": 0})
   ```

## After Internet
- Run code and show confusion matrix and classification report
- Optionally show a ROC curve:
```python
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
y_prob = model.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label=f'AUC = {auc(fpr, tpr):.2f}')
plt.plot([0,1],[0,1],'r--')
plt.xlabel('FPR'); plt.ylabel('TPR')
plt.title('ROC Curve'); plt.legend(); plt.show()
```
