# Visualization Libraries Demo
# Demonstrates: matplotlib, seaborn — different plot types

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============ CHANGE THESE ============
FILENAME = "data.csv"
NUM_COL1 = "col1"    # a numeric column
NUM_COL2 = "col2"    # another numeric column
CAT_COL = "category" # a categorical column
# ======================================

df = pd.read_csv(FILENAME)
print("Shape:", df.shape)
print(df.head())

# --- 1. Line Plot ---
plt.figure(figsize=(8, 4))
plt.plot(df[NUM_COL1], label=NUM_COL1)
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel(NUM_COL1)
plt.legend()
plt.tight_layout()
plt.show()

# --- 2. Scatter Plot ---
plt.figure(figsize=(8, 4))
plt.scatter(df[NUM_COL1], df[NUM_COL2], alpha=0.6)
plt.title("Scatter Plot")
plt.xlabel(NUM_COL1)
plt.ylabel(NUM_COL2)
plt.tight_layout()
plt.show()

# --- 3. Histogram ---
plt.figure(figsize=(8, 4))
plt.hist(df[NUM_COL1], bins=20, edgecolor='black')
plt.title("Histogram")
plt.xlabel(NUM_COL1)
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --- 4. Bar Plot (Seaborn) ---
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x=CAT_COL)
plt.title("Bar Plot - Category Counts")
plt.tight_layout()
plt.show()

# --- 5. Box Plot (Seaborn) ---
plt.figure(figsize=(8, 4))
sns.boxplot(data=df, x=CAT_COL, y=NUM_COL1)
plt.title("Box Plot")
plt.tight_layout()
plt.show()

# --- 6. Heatmap - Correlation ---
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# --- 7. Pair Plot ---
sns.pairplot(df.select_dtypes(include='number').iloc[:, :4])
plt.suptitle("Pair Plot", y=1.02)
plt.show()

print("All 7 plots generated successfully!")

"""
# --- CLEAN & PERFECT VISUALIZATION ---
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

# 1. Scatter (Numeric vs Numeric)
sns.scatterplot(x=df["col1"], y=df["col2"])
plt.show()

# 2. Bar (Category Counts)
sns.countplot(x=df["category"], data=df)
plt.show()

# 3. Correlation Heatmap
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.show()
"""
