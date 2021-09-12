
from libs.analyzer.regressions.abstract_regression import AbstractRegression
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.analyzer.analysis_model import AnalysisModel
from libs.analyzer.preprocessing.scalers import apply_scaler
from typing import Dict, Literal, Union


class AnalysisProvider:

    def __init__(self, analysis_model: AnalysisModel):
        self.__analysis_results: Dict[str, Union[str, int, float]] = {}
        self.__analysis_model: AnalysisModel = analysis_model

    def get_analysis_results(self) -> Dict[str, Union[str, int, float]]:
        return self.__analysis_results

    def scale_data(self, 
                   scaler_type: Literal['standard_scaler', 'min_max_scaler', 'maximum_absolute_scaler', 'robust_outlier_scaler', 'normalizer'] = None,
                   min_value: Union[int, float] = None, 
                   max_value: Union[int, float] = None,
                   norm: Literal['l1', 'l2', 'max'] = None) -> None:
        if scaler_type is None:
            return
        else:
            self.__analysis_model.X = apply_scaler(self.__analysis_model.X, scaler_type, min_value, max_value, norm)

    def regression(self, regressor_engine: AbstractRegression, *args) -> dict:
        regressor_engine.set_x(self.__analysis_model.X)
        regressor_engine.set_y(self.__analysis_model.Y)
        regressor_engine.train()
        regressor_engine.plot_model(*args)