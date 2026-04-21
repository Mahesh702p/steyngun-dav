# Visualization Libraries in R using ggplot2

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
NUM_COL1 <- "col1"     # numeric column
NUM_COL2 <- "col2"     # another numeric column
CAT_COL <- "category"  # categorical column
# ======================================

library(ggplot2)

df <- read.csv(FILENAME)
cat("Shape:", nrow(df), "x", ncol(df), "\n")
print(head(df))

# --- 1. Scatter Plot ---
print(ggplot(df, aes_string(x = NUM_COL1, y = NUM_COL2)) +
        geom_point(alpha = 0.6, color = "steelblue") +
        ggtitle("Scatter Plot") + theme_minimal())

# --- 2. Histogram ---
print(ggplot(df, aes_string(x = NUM_COL1)) +
        geom_histogram(bins = 20, fill = "steelblue", color = "black") +
        ggtitle("Histogram") + theme_minimal())

# --- 3. Bar Plot ---
print(ggplot(df, aes_string(x = CAT_COL)) +
        geom_bar(fill = "steelblue") +
        ggtitle("Bar Plot") + theme_minimal())

# --- 4. Box Plot ---
print(ggplot(df, aes_string(x = CAT_COL, y = NUM_COL1)) +
        geom_boxplot(fill = "lightblue") +
        ggtitle("Box Plot") + theme_minimal())

# --- 5. Line Plot ---
print(ggplot(df, aes_string(x = seq_len(nrow(df)), y = NUM_COL1)) +
        geom_line(color = "steelblue") +
        xlab("Index") + ggtitle("Line Plot") + theme_minimal())

# --- 6. Density Plot ---
print(ggplot(df, aes_string(x = NUM_COL1)) +
        geom_density(fill = "steelblue", alpha = 0.5) +
        ggtitle("Density Plot") + theme_minimal())

# --- 7. Correlation Heatmap (base R) ---
numeric_df <- df[sapply(df, is.numeric)]
cor_matrix <- cor(numeric_df, use = "complete.obs")
cat("\nCorrelation Matrix:\n")
print(round(cor_matrix, 2))
heatmap(cor_matrix, main = "Correlation Heatmap", scale = "none")

cat("\nAll plots generated!\n")
