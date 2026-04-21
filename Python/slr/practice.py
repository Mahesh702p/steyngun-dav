import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")
x = df["X"].values
y = df["Y"].values
n = len(x)
print(df.head())

x_mean = np.mean(x)
y_mean = np.mean(y)

num = np.sum((y-y_mean)*(x-x_mean))
den = np.sum((x-x_mean)**2)

m = num/den
c = y_mean-(m*x_mean)

y_pred = m*x + c

rss = np.sum((y-y_pred)**2)
tss = np.sum((y-y_mean)**2)

r_square = 1-(rss/tss)
rmse = np.sqrt(rss/n)

print(r_square)
print(rmse)

plt.scatter(x,y)
plt.plot(x,y_pred, color = 'black')
plt.savefig('regression_plot.png')

sns.regplot(x=x,y=y)

dir(pd)

