import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression , LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score

df = pd.read_csv("data.csv")
x = df[["col1","col2","col3"]]
y = df["target"]

x_train, x_test , y_train, y_test = train_test_split(x,y, test_size=0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

print(model.intercept_)
print(model.coef_)
print(r2_score(y_test, y_pred))
print(np.sqrt(mean_squared_error(y_test, y_pred)))

plt.scatter(y_test, y_pred, color='blue')
plt.axline((0,0), slope=1)
plt.savefig("mlr_result.png")




