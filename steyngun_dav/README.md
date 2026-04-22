# DAV Practical Exam — Cheat Sheet

## 📦 Imports to Remember
```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## 🐼 Pandas (Data Handling)

| Function | What It Does | Example |
|----------|-------------|---------|
| `pd.read_csv("file.csv")` | Load CSV into DataFrame | `df = pd.read_csv("data.csv")` |
| `df.head()` | First 5 rows | `df.head(10)` for first 10 |
| `df.shape` | (rows, columns) | `print(df.shape)` |
| `df.dtypes` | Data type of each column | |
| `df.describe()` | Stats: mean, std, min, max, quartiles | |
| `df.isnull().sum()` | Count missing values per column | |
| `df.fillna(value)` | Fill missing values | `df["col"].fillna(df["col"].median())` |
| `df.drop_duplicates()` | Remove duplicate rows | `df.drop_duplicates(inplace=True)` |
| `df.dropna()` | Drop rows with any NaN | |
| `df["col"]` | Select one column | Returns a Series |
| `df[["c1","c2"]]` | Select multiple columns | Returns a DataFrame |
| `df["col"].value_counts()` | Count unique values | Good for categorical |
| `df.select_dtypes(include='number')` | Only numeric columns | |
| `df.corr()` | Correlation matrix | |
| `df["col"].values` | Column as numpy array | |

---

## 🔢 NumPy (Math)

| Function | What It Does | Example |
|----------|-------------|---------|
| `np.mean(arr)` | Average | `np.mean(X)` |
| `np.sum(arr)` | Sum | `np.sum((X - x_mean)**2)` |
| `np.sqrt(x)` | Square root | `np.sqrt(mse)` |
| `np.array([...])` | Create array | `np.array([1,2,3])` |
| `arr.shape` | Dimensions | |

---

## 🤖 Scikit-Learn (ML)

### Train-Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

### Linear Regression
```python
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(model.coef_)        # coefficients
print(model.intercept_)   # intercept
```

### Logistic Regression
```python
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

### Metrics
| Function | For | Example |
|----------|-----|---------|
| `r2_score(y_true, y_pred)` | Regression | 0-1, higher = better |
| `mean_squared_error(y_true, y_pred)` | Regression | Lower = better |
| `mean_squared_error(..., squared=False)` | RMSE | |
| `accuracy_score(y_true, y_pred)` | Classification | 0-1 |
| `confusion_matrix(y_true, y_pred)` | Classification | TP, TN, FP, FN |
| `classification_report(y_true, y_pred)` | Classification | Precision, Recall, F1 |

---

## 📊 Matplotlib (Plotting)

```python
import matplotlib.pyplot as plt
```

| Plot Type | Code |
|-----------|------|
| **Line** | `plt.plot(x, y)` |
| **Scatter** | `plt.scatter(x, y)` |
| **Histogram** | `plt.hist(data, bins=20)` |
| **Bar** | `plt.bar(labels, values)` |

### Common Settings
```python
plt.title("Title")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.tight_layout()
plt.show()
```

### Subplots
```python
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].plot(x, y)
axes[0].set_title("Plot 1")
```

---

## 🎨 Seaborn (Statistical Plots)

```python
import seaborn as sns
```

| Plot | Code | Use For |
|------|------|---------|
| **Heatmap** | `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')` | Correlation |
| **Box Plot** | `sns.boxplot(x="cat", y="num", data=df)` | Distribution + outliers |
| **Bar Count** | `sns.countplot(x="col", data=df)` | Category counts |
| **Pair Plot** | `sns.pairplot(df)` | All scatter plots at once |
| **Dist Plot** | `sns.histplot(df["col"], kde=True)` | Distribution + curve |

---

## ⏱️ Statsmodels (ARIMA)

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(train_data, order=(1,1,1))
fitted = model.fit()
print(fitted.summary())
forecast = fitted.forecast(steps=10)
```

---

## 📝 Text Analytics

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Word Frequency
cv = CountVectorizer(stop_words='english')
matrix = cv.fit_transform(df["text"])
words = cv.get_feature_names_out()

# TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
matrix = tfidf.fit_transform(df["text"])

# Sentiment
from textblob import TextBlob
blob = TextBlob("some text")
blob.sentiment.polarity   # -1 to +1
```

---

## 🚀 Quick Install (run after getting internet)

```bash
pip install pandas numpy scikit-learn matplotlib seaborn statsmodels textblob
python -m textblob.download_corpora
```
