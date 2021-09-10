import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

dati = pd.read_csv("https://raw.githubusercontent.com/lucafont88/test_automatic_repo/storing/eurusd_test_fx1.csv")


# print(dati.head())

# Dataset
X = list(dati['index'])
Y = list(dati['close'])
np_X = np.array(X).reshape(len(X), 1)
np_Y = np.array(Y).reshape(len(Y), 1)

# Regression model
reg = linear_model.LinearRegression()
reg.fit(np_X, np_Y)

# Print out computed linear model
print("Linear Regression Coefficents:")
print(reg.coef_)
print("------------------------------")
print("Linear Regression Intercept:")
print(reg.intercept_)
print("------------------------------")
print("Linear Regression Prameters:")
print(reg.get_params())
print("------------------------------")

# Predict with the linear model
prediction = reg.predict(np_X)

# Plotting
fig, axs = plt.subplots()  # Create a figure and an axes.
axs.plot(list(dati['index']), list(dati['high']), label='High')
axs.plot(list(dati['index']), list(dati['low']), label='Low')
axs.set_xlabel('tick')  # Add an x-label to the axes.
axs.set_ylabel('normalized value')  # Add a y-label to the axes.
axs.set_title("TEST Forex")  # Add a title to the axes.
axs.legend()  # Add a legend.

fig_regression, axs_regression = plt.subplots()
scatter_size = 2
axs_regression.set_title("Linear Regression")
axs_regression.set_xlabel("X")
axs_regression.set_ylabel("Y")
axs_regression.scatter(np_X[:], np_Y[:], s=scatter_size, color='red')
axs_regression.plot(np_X[:], prediction, '-')

plt.show()
