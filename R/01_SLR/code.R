# Simple Linear Regression - FROM SCRATCH (No libraries)
# Only base R used — no lm() function
# Formula: y = mx + c

# ============ CHANGE THESE ============
FILENAME <- "data.csv"
X_COL <- "X"    # independent variable column
Y_COL <- "Y"    # dependent variable column
# ======================================

# --- Read CSV ---
df <- read.csv(FILENAME)
X <- df[[X_COL]]
Y <- df[[Y_COL]]
n <- length(X)
cat("Loaded", n, "data points\n")

# --- Calculate Means ---
x_mean <- mean(X)
y_mean <- mean(Y)
cat("Mean of X:", round(x_mean, 4), "\n")
cat("Mean of Y:", round(y_mean, 4), "\n")

# --- Calculate m (slope) and c (intercept) ---
numerator <- sum((X - x_mean) * (Y - y_mean))
denominator <- sum((X - x_mean)^2)

m <- numerator / denominator
c <- y_mean - m * x_mean
cat("\nRegression Equation: y =", round(m, 4), "* x +", round(c, 4), "\n")

# --- Predictions ---
Y_pred <- m * X + c

# --- R-squared ---
ss_res <- sum((Y - Y_pred)^2)
ss_tot <- sum((Y - y_mean)^2)
r_squared <- 1 - (ss_res / ss_tot)
cat("R-squared:", round(r_squared, 4), "\n")

# --- RMSE ---
rmse <- sqrt(ss_res / n)
cat("RMSE:", round(rmse, 4), "\n")

# --- Predict new value ---
cat("\nEnter X value to predict Y: ")
x_new <- as.numeric(readline())
y_new <- m * x_new + c
cat("Predicted Y for X =", x_new, ":", round(y_new, 4), "\n")

# --- Print first 5 ---
cat("\n--- First 5 Actual vs Predicted ---\n")
for (i in 1:min(5, n)) {
  cat("X =", round(X[i], 2), " Actual Y =", round(Y[i], 2),
      " Predicted Y =", round(Y_pred[i], 2), "\n")
}

# --- CLEAN & PERFECT SLR (Using lm()) ---
# df <- read.csv("data.csv")
# model <- lm(Y ~ X, data = df)
# print(summary(model))

# # Visualization
# plot(df$X, df$Y, col="blue", main="SLR")
# abline(model, col="red")
