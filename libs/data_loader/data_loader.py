import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

dati = pd.read_csv("https://raw.githubusercontent.com/lucafont88/test_automatic_repo/storing/eurusd_test_fx1.csv")


print(dati.head())

fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(list(dati['index']), list(dati['high']), label='High')
ax.plot(list(dati['index']), list(dati['low']), label='Low')
ax.set_xlabel('tick')  # Add an x-label to the axes.
ax.set_ylabel('normalized value')  # Add a y-label to the axes.
ax.set_title("TEST Forex")  # Add a title to the axes.
ax.legend()  # Add a legend.

plt.show()