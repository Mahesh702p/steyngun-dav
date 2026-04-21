# 🎤 DAV Practical Viva Prep Guide

This guide covers the most frequent questions asked during the DAV lab viva.

---

## 1. Library Basics (Crucial!)

**Q: Why use Pandas over Excel?**
*   **A:** Pandas can handle much larger datasets (millions of rows) efficiently, allows easy automation with code, and integrates directly with Machine Learning libraries.

**Q: What is the difference between a Series and a DataFrame?**
*   **A:** A **Series** is a 1D array (like a single column). A **DataFrame** is a 2D table (multiple columns/rows).

**Q: Why use NumPy instead of Python lists?**
*   **A:** NumPy arrays are **faster** and use **less memory**. They allow "vectorized" operations (applying math to the whole array at once).

**Q: Difference between Matplotlib and Seaborn?**
*   **A:** Matplotlib is for basic, low-level plotting. Seaborn is built on top of it and provides high-level, beautiful statistical plots (like heatmaps and boxplots) with simpler code.

---

## 2. Data Cleaning Questions

**Q: What is the difference between `loc` and `iloc`?**
*   **A:** `loc` is **Label-based** (using column names). `iloc` is **Index-based** (using integer positions like 0, 1, 2).

**Q: How do you handle missing (NaN) values?**
*   **A:** Two ways: `df.dropna()` (remove them) or `df.fillna()` (replace them with the **mean, median, or mode**).

---

## 3. Machine Learning Questions

**Q: Why do we use `train_test_split`?**
*   **A:** To evaluate the model. We train it on one part and test it on "unseen" data to see if it actually learned or just memorized.

**Q: What is `random_state`?**
*   **A:** It ensures the data split is the same every time you run the code. This makes your results **reproducible**.

**Q: Explain the difference between `fit()`, `predict()`, and `score()`.**
*   **A:**
    *   **`fit()`**: Training the model (learning from data).
    *   **`predict()`**: Using the trained model to get results for new data.
    *   **`score()`**: Calculating the accuracy or R-squared.

**Q: When do we use Linear vs Logistic Regression?**
*   **A:** **Linear** is for predicting a continuous number (e.g., Price, Temp). **Logistic** is for classification (e.g., Yes/No, 0/1).

---

## 4. Specific Methods (Tips & Tricks)

**Q: What is R-squared ($R^2$)?**
*   **A:** It measures the "Goodness of Fit". A value closer to 1 means the model explains the data very well.

**Q: What are the parameters (p, d, q) in ARIMA?**
*   **A:** 
    *   **p**: Auto-Regressive (past values).
    *   **d**: Integrated (making data stationary).
    *   **q**: Moving Average (past errors).

**Q: What does `dir()` do?**
*   **A:** It lists all methods and attributes available for an object. It’s useful for finding functions you’ve forgotten!
