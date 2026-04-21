# Data Cleaning + Visualization in R

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
# ======================================

library(ggplot2)

# ===================== PART 1: DATA CLEANING =====================

df <- read.csv(FILENAME)
cat("=== Original Data ===\n")
cat("Shape:", nrow(df), "x", ncol(df), "\n")
print(head(df))

# --- 1. Missing Values ---
cat("\n=== Missing Values ===\n")
print(colSums(is.na(df)))

# --- 2. Fill Missing Values ---
for (col in names(df)) {
  if (is.numeric(df[[col]])) {
    df[[col]][is.na(df[[col]])] <- median(df[[col]], na.rm = TRUE)
  } else {
    mode_val <- names(sort(table(df[[col]]), decreasing = TRUE))[1]
    df[[col]][is.na(df[[col]])] <- mode_val
  }
}
cat("\nAfter filling:\n")
print(colSums(is.na(df)))

# --- 3. Remove Duplicates ---
before <- nrow(df)
df <- unique(df)
cat("\nRemoved", before - nrow(df), "duplicates\n")

# --- 4. Summary ---
cat("\n=== Summary Statistics ===\n")
print(summary(df))

cat("\nCleaned Shape:", nrow(df), "x", ncol(df), "\n")

# ===================== PART 2: VISUALIZATION =====================

numeric_cols <- names(df)[sapply(df, is.numeric)]
cat_cols <- names(df)[sapply(df, is.character)]

# --- Histogram ---
if (length(numeric_cols) > 0) {
  print(ggplot(df, aes_string(x = numeric_cols[1])) +
          geom_histogram(bins = 20, fill = "steelblue", color = "black") +
          ggtitle(paste("Distribution of", numeric_cols[1])) + theme_minimal())
}

# --- Correlation Heatmap ---
if (length(numeric_cols) > 1) {
  cor_mat <- cor(df[numeric_cols], use = "complete.obs")
  heatmap(cor_mat, main = "Correlation Heatmap", scale = "none")
}

# --- Bar Plot ---
if (length(cat_cols) > 0) {
  print(ggplot(df, aes_string(x = cat_cols[1])) +
          geom_bar(fill = "steelblue") +
          ggtitle(paste("Counts of", cat_cols[1])) + theme_minimal() +
          theme(axis.text.x = element_text(angle = 45, hjust = 1)))
}

# --- Box Plot ---
if (length(numeric_cols) > 0 && length(cat_cols) > 0) {
  print(ggplot(df, aes_string(x = cat_cols[1], y = numeric_cols[1])) +
          geom_boxplot(fill = "lightblue") +
          ggtitle(paste(numeric_cols[1], "by", cat_cols[1])) + theme_minimal() +
          theme(axis.text.x = element_text(angle = 45, hjust = 1)))
}

cat("\nData cleaning and visualization complete!\n")
