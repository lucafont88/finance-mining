from typing import Dict, List, Union
import numpy as np
import random
import matplotlib
import matplotlib.pyplot as plt

from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline, make_pipeline


class InterpolationEngine:

    def __init__(self, np_data: np.ndarray, interpolations_degrees: List[int] = [3, 4, 5], n_interpolation_step: int = 10):
        self.np_data = np_data
        self.interpolations_degrees = interpolations_degrees
        self.n_interpolation_step = n_interpolation_step

    def create_interpolation_model(self) -> Dict[int, Pipeline]:
        self.x_train = self.__compute_inteporlation_linespace()
        rng = np.random.RandomState(0)
        rng.shuffle(self.x_train)
        self.x_train = np.sort(self.x_train[:20])
        y = self.__f(self.x_train)
        X = self.x_train[:, np.newaxis]
        models: Dict[int, Pipeline] = {}
        for degree in range(min(self.interpolations_degrees), max(self.interpolations_degrees) + 1): # Default is [3, 4, 5]
            model = make_pipeline(PolynomialFeatures(degree), Ridge())
            model.fit(X, y)
            models[degree] = model
        self.models = models
        return models

    def plot_interpolation_model(self, degrees: List[int] = [3, 4, 5], do_plot: bool = False) -> plt.Figure:
        # generate points used to plot
        x_plot = self.__compute_inteporlation_linespace()
        X_plot = x_plot[:, np.newaxis]
        colors = self.__get_colors()
        # colors = ['gold', 'teal', 'yellowgreen', 'pink', 'red'] # TODO: Change to a list of colors accordig to input
        lw = 2
        fig = plt.figure(figsize=(5, 4))
        plt.plot(x_plot, self.__f(x_plot), color='cornflowerblue', linewidth=lw, label="ground truth")
        plt.scatter(self.x_train, self.__f(self.x_train), color='navy', s=30, marker='o', label="training points")
        count = 0
        
        for degree in degrees:
            y_plot = self.models[degree].predict(X_plot)
            plt.plot(x_plot, y_plot, color=colors[count], linewidth=lw, label="degree %d" % degree)
            count += 1
        plt.legend(loc='lower left')
        if do_plot:
            plt.show()
            
        return fig
        



    # Private methods

    def __compute_inteporlation_linespace(self) -> np.ndarray:
        return np.linspace(0, len(self.np_data), self.n_interpolation_step, dtype=int)

    def __f(self, x: List[int]) -> Union[int, float]:
        if max(x) < self.np_data.shape[0]:
            return self.np_data[x, 1]
        else:
            return self.np_data[x - 1, 1]

    __colors = []
    def __get_colors(self) -> List[str]:
        if len(self.__colors) > 0:
            return self.__colors
        self.__colors = list((matplotlib.colors.get_named_colors_mapping()).values())
        random.shuffle(self.__colors)
        return self.__colors
