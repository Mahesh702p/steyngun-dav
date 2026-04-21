# Text Analytics - Variant 2: Sentiment Analysis in R
# Uses syuzhet package for sentiment scoring

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
TEXT_COL <- "text"
# ======================================

library(syuzhet)

# --- Load ---
df <- read.csv(FILENAME, stringsAsFactors = FALSE)
cat("Loaded", nrow(df), "rows\n")

# --- Sentiment Scores ---
sentiments <- get_sentiment(df[[TEXT_COL]], method = "syuzhet")
df$Polarity <- sentiments
df$Sentiment <- ifelse(sentiments > 0, "Positive",
                       ifelse(sentiments < 0, "Negative", "Neutral"))

# --- Distribution ---
cat("\n--- Sentiment Distribution ---\n")
print(table(df$Sentiment))
cat("\nAverage Polarity:", round(mean(df$Polarity), 4), "\n")

# --- Sample ---
cat("\n--- Sample Results ---\n")
print(head(df[, c(TEXT_COL, "Sentiment", "Polarity")], 10))
