

from sklearn.pipeline import Pipeline
from libs.configuration.configuration_reader import ConfigurationReader
from libs.security.secret_manager import SecretManager
from libs.data_output.file_saver import FileSaver
from libs.analyzer.polynomial.polynomial_engine import PolynomialEngine
from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult
from libs.analyzer.statistical.statistical_analyzer import StatisticalAnalyzer
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.utility.helpers import get_numpy_2d_array, merge_dicts
from libs.analyzer.analysis_provider import AnalysisProvider
from libs.analyzer.analysis_model import AnalysisModel
from libs.analyzer.preprocessing.scalers import ScalerModel
from libs.plotting.plot_engine import PlotEngine
from libs.plotting.plot_model import Axis, PlotModel
from typing import Any, Dict, List, Literal, Union
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pprint
from libs.data_loader.data_loader_provider import DataLoaderProvider
from icecream import ic

class LinearAnalyzerEngine:

    def __init__(self, secret_manager: SecretManager, configuration_reader: ConfigurationReader, prompt_debug: bool = False):
        self.__data_loader_provider = DataLoaderProvider(secret_manager)
        self.__confguration_reader = configuration_reader
        self.__PROMPT_DEBUG = prompt_debug

    def run(self, 
            csv_file_to_load, feature_to_analyze: Literal['open', 'high', 'low', 'close', 'volume'], 
            index_key: str = 'index') -> Union[DescribeResult, RelfreqResult, CumfreqResult, Dict[str, Any], Dict[int, Pipeline], PlotModel]:
        self.__load(csv_file_to_load)
        stats, rel_freq_result, cum_freq_result, model_info, poly_models, poly_models_figure, plot_model = self.__analyze(feature_to_analyze, index_key)
        self.__plot()
        return stats, rel_freq_result, cum_freq_result, model_info, poly_models, poly_models_figure, plot_model


    #Private methods

    def __load(self, csv_file_to_load) -> None:
        data = self.__data_loader_provider.load_data(csv_file_to_load)
        self.__data: pd.DataFrame = data[0]

    def __analyze(self, 
                feature_to_analyze: Literal['open', 'high', 'low', 'close', 'volume'], 
                index_key: str = 'index') -> Union[DescribeResult, RelfreqResult, CumfreqResult, Dict[str, Any], Dict[int, Pipeline], PlotModel]:
        axis: Axis = Axis(feature_to_analyze, list(self.__data[index_key]), list(self.__data[feature_to_analyze]))
        self.__plot_model = PlotModel('EurUsd daily 1min', 'tick', 'price', [axis])
        
        # Mono analisi
        x1 = axis.x
        y1 = axis.y
        scaler_model = ScalerModel('min_max_scaler', -1, 1, None)
        analysys_model: AnalysisModel = AnalysisModel('test_analisi_1', x1, y1)
        analysis_provider: AnalysisProvider = AnalysisProvider(analysys_model)
        scaled_y = analysis_provider.scale_data(scaler_model)

        # Numpy dataset creation: Shape = (len(x1), 2)
        np_dataset = get_numpy_2d_array(x1, scaled_y[:, 0])
        if self.__PROMPT_DEBUG is True:
            ic(np_dataset)

        # Statistical Analysis
        stats: DescribeResult = StatisticalAnalyzer.analyze(scaled_y)
        rel_freq_result: RelfreqResult = StatisticalAnalyzer.relative_frequency(scaled_y, 100, False)
        cum_freq_result: CumfreqResult = StatisticalAnalyzer.cumulated_frequency(scaled_y, 50, False)

        entropy: float = StatisticalAnalyzer.calculate_entropy(scaled_y)

        # # TODO Da sistemare
        # if np.isinf(entropy[0]):
        #     model_info['entropy'] = 'NA'
        # if abs(entropy[0]) > 0.0001:
        #     model_info['entropy'] = entropy[0]
        # else:
        #     model_info['entropy'] = 'NA'


        # Linear regression
        linear_regression_model = analysis_provider.regression(LinearRegression(), False)

        # Gather information in a dictionary
        model_info: Dict[str, Any] = merge_dicts(linear_regression_model.get_model_informations(), stats._asdict())

        # Fit polynomial model 
        INTERPOLATION_DEGREES: List[int] = self.__confguration_reader.get_interpolation_degree_list()
        INTERPOLATION_N_POINTS: int = self.__confguration_reader.get_interpolation_n_samples() 
        polynomial_engine = PolynomialEngine()
        poly, x_poly = polynomial_engine.compute_polynomial_features(np_dataset, 2)
        poly_models, poly_models_figure = polynomial_engine.compute_interpolated_polynomial(np_dataset, INTERPOLATION_DEGREES, INTERPOLATION_N_POINTS, False)
    
        # Print model information
        pp = pprint.PrettyPrinter(depth=4)
        pp.pprint(model_info)

        # Save model as json on file
        OUTPUT_FILE: str = self.__confguration_reader.get_secret(self.__confguration_reader.OUTPUT_FILE_TOKEN)
        file_saver = FileSaver(OUTPUT_FILE)
        file_saver.save_json(model_info)

        # Prompt debug if required
        self.__prompt_debug(np_dataset, linear_regression_model, stats, rel_freq_result, cum_freq_result, entropy, x_poly)

        # Return dictionary with model information
        return stats, rel_freq_result, cum_freq_result, model_info, poly_models, poly_models_figure, self.__plot_model

    def __plot(self):
        SHOW_PLOTS = False
        if SHOW_PLOTS is True:
            plot_engine = PlotEngine()
            plot_engine.plot(self.__plot_model)
            plt.show()

    def __prompt_debug(self, 
                    np_dataset: np.ndarray, 
                    linear_regression_model: LinearRegression,
                    stats: DescribeResult,
                    rel_freq_result: RelfreqResult,
                    cum_freq_result: CumfreqResult,
                    entropy: float,
                    x_poly: Any):
        if self.__PROMPT_DEBUG is True:
            ic(np_dataset)
            print(f'Model: {linear_regression_model.get_model_informations()}')
            print(stats)
            print(f"Entropia {entropy}")
            print(f"Relative frequency: {rel_freq_result}")
            print(f"Cumulated frequency: {cum_freq_result}")
            print(f"Computed polynomial features (expected (n, 2)) = {x_poly.shape}")