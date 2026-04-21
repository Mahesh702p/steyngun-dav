# # Multiple Linear Regression in R using lm()

# # ============ CHANGE THESE ============
# FILENAME <- "data.csv"
# TARGET <- "target"   # dependent variable
# # ======================================

# # --- Load ---
# df <- read.csv(FILENAME)
# cat("Shape:", nrow(df), "x", ncol(df), "\n")
# print(head(df))

# # --- Train/Test Split (80/20) ---
# set.seed(42)
# idx <- sample(1:nrow(df), 0.8 * nrow(df))
# train <- df[idx, ]
# test <- df[-idx, ]
# cat("\nTrain:", nrow(train), "Test:", nrow(test), "\n")

# # --- Fit Model (. means all other columns as predictors) ---
# formula <- as.formula(paste(TARGET, "~ ."))
# model <- lm(formula, data = train)
# print(summary(model))

# # --- Predict ---
# y_pred <- predict(model, newdata = test)
# y_actual <- test[[TARGET]]

# # --- Evaluate ---
# rmse <- sqrt(mean((y_actual - y_pred)^2))
# ss_res <- sum((y_actual - y_pred)^2)
# ss_tot <- sum((y_actual - mean(y_actual))^2)
# r_squared <- 1 - ss_res / ss_tot

# cat("\nR-squared:", round(r_squared, 4), "\n")
# cat("RMSE:", round(rmse, 4), "\n")

#   cat("Actual:", round(y_actual[i], 2), " Predicted:", round(y_pred[i], 2), "\n")
# }

# --- CLEAN & PERFECT MLR ---
df <- read.csv("data.csv")
model <- lm(target ~ ., data = df)
print(summary(model))

# Visualization (Actual vs Predicted)
plot(df$target, predict(model), col="blue", main="Actual vs Predicted")
abline(0, 1, col="red")
