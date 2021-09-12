from libs.analyzer.regressions.abstract_regression import AbstractRegression
from typing import List
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

class LinearRegression(AbstractRegression):
    def __init__(self):
        super().__init__()

    def set_x(self, x: List[float]) -> None:
        self.X = x

    def set_y(self, y: List[float]) -> None:
        self.Y = y

    def train(self):
        # Reshaping data
        self.np_X = np.array(self.X).reshape(len(self.X), 1)
        self.np_Y = np.array(self.Y).reshape(len(self.Y), 1)

        # Regression model
        self.reg = linear_model.LinearRegression()
        self.reg.fit(self.np_X, self.np_Y)

    def predict(self, x: float):
        return self.reg.predict(x)

    def get_model(self) -> linear_model.LinearRegression:
        return self.reg

    def get_model_informations(self) -> dict:
        return {
            'linear_regression_coefficents': self.reg.coef_,
            'linear_regression_intercept': self.reg.intercept_,
            'linear_regression_parameters': self.reg.get_params()
        }
        
    def plot_model(self, title: str = 'Linear Regression Model', x_label: str = 'X', y_label: str = 'Y', scatter_size: int = 2, scatter_color: str = 'red'):
        fig, axs = plt.subplots()
        scatter_size = 2
        axs.set_title(title)
        axs.set_xlabel(x_label)
        axs.set_ylabel(y_label)
        prediction = self.reg.predict(self.np_X)
        axs.scatter(self.np_X[:], self.np_Y[:], s=scatter_size, color=scatter_color)
        axs.plot(self.np_X[:], prediction, '-')
