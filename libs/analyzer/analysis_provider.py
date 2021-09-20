
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.analyzer.analysis_model import AnalysisModel
from libs.analyzer.preprocessing.scalers import ScalerModel, apply_scaler
from typing import Dict, List, Union
import matplotlib.pyplot as plt 

class AnalysisProvider:

    def __init__(self, analysis_model: AnalysisModel):
        self.__analysis_results: Dict[str, Union[str, int, float]] = {}
        self.__analysis_model: AnalysisModel = analysis_model

    def get_analysis_results(self) -> Dict[str, Union[str, int, float]]:
        return self.__analysis_results

    def scale_data(self, 
                   scaler_model: ScalerModel,
                   return_scaled_data: bool = True) -> Union[List[Union[float, int]], None]:
        if scaler_model.scaler_type is not None:
            scaler_model: ScalerModel = ScalerModel(scaler_model.scaler_type, scaler_model.min_value, scaler_model.max_value, scaler_model.norm)
            self.__analysis_model.Y = apply_scaler(self.__analysis_model.Y, scaler_model)

        if return_scaled_data is True:
            return self.__analysis_model.Y
        else:
            return None

    def regression(self, linear_regressor_engine: LinearRegression, **kwargs) -> Union[LinearRegression, plt.Figure]:
        linear_regressor_engine.set_x(self.__analysis_model.X)
        linear_regressor_engine.set_y(self.__analysis_model.Y)
        linear_regressor_engine.train()
        figure = linear_regressor_engine.plot_model(**kwargs)
        return linear_regressor_engine, figure