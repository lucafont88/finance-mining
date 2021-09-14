from libs.analyzer.polynomial.polynomial_engine import PolynomialEngine
from numpy import inf
from libs.data_output.file_saver import FileSaver
from libs.analyzer.preprocessing.scalers import ScalerModel
from libs.data_loader.data_loader_provider import DataLoaderProvider
from libs.analyzer.analysis_provider import AnalysisProvider
from libs.analyzer.analysis_model import AnalysisModel
from scipy.stats.stats import CumfreqResult, RelfreqResult
from libs.analyzer.statistical.statistical_analyzer import StatisticalAnalyzer
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.plotting.plot_engine import PlotEngine
from libs.plotting.plot_model import Axis, PlotModel
from libs.utility.helpers import get_numpy_2d_array, merge_dicts
from typing import Any, Dict, List
import pandas as pd
import matplotlib.pyplot as plt
import pprint
import numpy as np
from icecream import ic


PROMPT_DEBUG = False
SHOW_PLOTS = False
OUTPUT_FILE = './output_results.json'
SECRET_FILE = './secrets.txt'
CSV_TO_LOAD_FILE = './resourse_to_load.txt'
data_loader_provider = DataLoaderProvider(SECRET_FILE, CSV_TO_LOAD_FILE)
data = data_loader_provider.load_data()

intraday: pd.DataFrame = data[0]
# daily: pd.DataFrame = data[1]

axis_1: Axis = Axis('High', list(intraday['index']), list(intraday['high']))
axis_2: Axis = Axis('Low', list(intraday['index']), list(intraday['low']))

axis_list: List[Axis] = [axis_1, axis_2]

plot_model = PlotModel('EurUsd daily 1min', 'tick', 'price', axis_list)
plot_engine = PlotEngine()
plot_engine.plot(plot_model)

# Mono analisi
x1 = axis_1.x
y1 = axis_1.y
scaler_model = ScalerModel('min_max_scaler', -1, 1, None)
analysys_model: AnalysisModel = AnalysisModel('test_analisi_1', x1, y1)
analysis_provider: AnalysisProvider = AnalysisProvider(analysys_model)
scaled_y = analysis_provider.scale_data(scaler_model)

# Shape = (len(x1), 2)
np_dataset = get_numpy_2d_array(x1, scaled_y[:, 0])
ic(np_dataset)


linear_regression_model = analysis_provider.regression(LinearRegression())

stats = StatisticalAnalyzer.analyze(scaled_y)
entropy: float = StatisticalAnalyzer.calculate_entropy(scaled_y)

model_info: Dict[str, Any] = merge_dicts(linear_regression_model.get_model_informations(), stats._asdict())

# TODO Da sistemare
if np.isinf(entropy[0]):
    model_info['entropy'] = 'NA'
if abs(entropy[0]) > 0.0001:
    model_info['entropy'] = entropy[0]
else:
    model_info['entropy'] = 'NA'

if PROMPT_DEBUG is True:
    print(f'Model: {linear_regression_model.get_model_informations()}')
    print(stats)
    print(f"Entropia {entropy}")

rel_freq_result: RelfreqResult = StatisticalAnalyzer.relative_frequency(scaled_y, 100, True)
cum_freq_result: CumfreqResult = StatisticalAnalyzer.cumulated_frequency(scaled_y, 50, True)

if PROMPT_DEBUG is True:
    print(f"Relative frequency: {rel_freq_result}")
    print(f"Cumulated frequency: {cum_freq_result}")

# TODO Polynomial Fitting
polynomial_engine = PolynomialEngine()
poly, x_poly = polynomial_engine.fit_polynomial(scaled_y, None, 2)

ic(poly.powers_)
ic(x_poly)

# Output

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(model_info)

file_saver = FileSaver(OUTPUT_FILE)
file_saver.save_json(model_info)

if SHOW_PLOTS is True:
    plt.show()
