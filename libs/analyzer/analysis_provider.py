
from libs.analyzer.regressions.abstract_regression import AbstractRegression
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.analyzer.analysis_model import AnalysisModel
from typing import Dict, Union


class AnalysisProvider:

    def __init__(self, analysis_model: AnalysisModel):
        self.__analysis_results: Dict[str, Union[str, int, float]] = {}
        self.__analysis_model: AnalysisModel = analysis_model

    def get_analysis_results(self) -> Dict[str, Union[str, int, float]]:
        return self.__analysis_results

    def regression(self, regressor_engine: AbstractRegression, *args) -> dict:
        regressor_engine.set_x(self.__analysis_model.X)
        regressor_engine.set_y(self.__analysis_model.Y)
        regressor_engine.train()
        regressor_engine.plot_model(*args)