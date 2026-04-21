# Data Cleaning + Visualization

## What It Is
A two-part experiment: first clean a raw/messy dataset (handle missing values, duplicates, data types), then apply visualizations on the cleaned data.

## Cleaning Steps Done
1. **Check missing values** — `df.isnull().sum()`
2. **Fill missing values** — median for numeric, mode for categorical
3. **Remove duplicates** — `drop_duplicates()`
4. **Inspect data types** — ensure columns have correct types
5. **Summary statistics** — `df.describe()`

## Key Concepts to Mention
- **Why median over mean?** — median is robust to outliers
- **Why mode for categorical?** — fills with most common value
- **Duplicates** can skew analysis and ML models
- **EDA (Exploratory Data Analysis)** = cleaning + visualization together

## Libraries Needed
```bash
pip install pandas matplotlib seaborn
```

## How to Adapt
1. Just change `FILENAME` — the code **auto-detects** numeric and categorical columns
2. No need to specify column names — it works with any CSV

## After Internet
- Install and run — it will print cleaning info and show 4 plots
- The auto-detection makes this code work with almost any dataset without changes

## Tip
Sir may ask "why not drop rows with missing values?" — Answer: "Dropping rows loses data. Imputation (filling with median/mode) preserves the sample size, which is important for smaller datasets."
