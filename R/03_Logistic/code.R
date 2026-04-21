# Logistic Regression in R using glm()
# For binary classification (0/1)

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
TARGET <- "target"   # binary column (0 or 1)
# ======================================

# --- Load ---
df <- read.csv(FILENAME)
cat("Shape:", nrow(df), "x", ncol(df), "\n")
cat("Target distribution:\n")
print(table(df[[TARGET]]))

# --- Train/Test Split ---
set.seed(42)
idx <- sample(1:nrow(df), 0.8 * nrow(df))
train <- df[idx, ]
test <- df[-idx, ]

# --- Fit Logistic Regression ---
formula <- as.formula(paste(TARGET, "~ ."))
model <- glm(formula, data = train, family = binomial)
print(summary(model))

# --- Predict ---
prob <- predict(model, newdata = test, type = "response")
y_pred <- ifelse(prob > 0.5, 1, 0)
y_actual <- test[[TARGET]]

# --- Confusion Matrix ---
conf_matrix <- table(Predicted = y_pred, Actual = y_actual)
cat("\nConfusion Matrix:\n")
print(conf_matrix)

accuracy <- sum(y_pred == y_actual) / length(y_actual)
cat("\nAccuracy:", round(accuracy, 4), "\n")



# --- CLEAN & PERFECT LOGISTIC ---
# df <- read.csv("data.csv")
# model <- glm(target ~ ., data = df, family = binomial)
# p <- predict(model, type="response")
# plot(p, main="Probabilities")
