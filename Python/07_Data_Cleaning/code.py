# Data Cleaning + Visualization
# Steps: Load → Inspect → Clean → Visualize

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============ CHANGE THESE ============
FILENAME = "data.csv"
# ======================================

# ===================== PART 1: DATA CLEANING =====================

# --- Load ---
df = pd.read_csv(FILENAME)
print("=== Original Data ===")
print(f"Shape: {df.shape}")
print(df.head())

# --- 1. Check for Missing Values ---
print("\n=== Missing Values ===")
print(df.isnull().sum())

# --- 2. Handle Missing Values ---
# Fill numeric columns with median, categorical with mode
for col in df.columns:
    if df[col].dtype in ['float64', 'int64']:
        df[col].fillna(df[col].median(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nAfter filling missing values:")
print(df.isnull().sum())

# --- 3. Remove Duplicates ---
before = len(df)
df.drop_duplicates(inplace=True)
print(f"\nRemoved {before - len(df)} duplicate rows")

# --- 4. Check Data Types ---
print("\n=== Data Types ===")
print(df.dtypes)

# --- 5. Basic Statistics ---
print("\n=== Statistics ===")
print(df.describe())

print(f"\nCleaned Shape: {df.shape}")

# ===================== PART 2: VISUALIZATION =====================

numeric_cols = df.select_dtypes(include='number').columns.tolist()
cat_cols = df.select_dtypes(include='object').columns.tolist()

# --- Histogram of first numeric column ---
if numeric_cols:
    plt.figure(figsize=(8, 4))
    plt.hist(df[numeric_cols[0]], bins=20, edgecolor='black')
    plt.title(f"Distribution of {numeric_cols[0]}")
    plt.xlabel(numeric_cols[0])
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# --- Correlation Heatmap ---
if len(numeric_cols) > 1:
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.show()

# --- Bar plot of first categorical column ---
if cat_cols:
    plt.figure(figsize=(8, 4))
    df[cat_cols[0]].value_counts().head(10).plot(kind='bar')
    plt.title(f"Top 10 Categories in {cat_cols[0]}")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()

# --- Box plot ---
if numeric_cols and cat_cols:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df, x=cat_cols[0], y=numeric_cols[0])
    plt.title(f"{numeric_cols[0]} by {cat_cols[0]}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\nData cleaning and visualization complete!")

"""
# --- CLEAN & PERFECT DATA CLEANING ---
import pandas as pd

df = pd.read_csv("data.csv")

# 1. Handle Missing Values (Numeric: Median, Categorical: Mode)
df.fillna(df.median(numeric_only=True), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)

# 2. Remove Duplicates
df.drop_duplicates(inplace=True)

# 3. Check types and stats
print(df.info())
print(df.describe())
"""
