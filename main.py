from libs.data_loader.data_loader_provider import DataLoaderProvider
from libs.analyzer.analysis_provider import AnalysisProvider
from libs.analyzer.analysis_model import AnalysisModel
from scipy.stats.stats import CumfreqResult, RelfreqResult
from libs.analyzer.statistical.statistical_analyzer import StatisticalAnalyzer
from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.plotting.plot_engine import PlotEngine
from libs.plotting.plot_model import Axis, PlotModel
from typing import List
from libs.data_loader.file_to_load_reader import FileToLoadReader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from libs.utility.secret_manager import SecretManager
from libs.data_loader.data_loader import DataLoader

SECRET_FILE = './secrets.txt'
CSV_TO_LOAD_FILE = './resourse_to_load.txt'
data_loader_provider = DataLoaderProvider(SECRET_FILE, CSV_TO_LOAD_FILE)
data = data_loader_provider.load_data()


# i = 1
# for data_frame in data:
#     print(f'Data Frame {i}:')
#     print(data_frame.head())
#     i += 1

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

analysys_model: AnalysisModel = AnalysisModel('test_analisi_1', x1, y1)
analysis_provider: AnalysisProvider = AnalysisProvider(analysys_model)
linear_regression_model = LinearRegression()
analysis_provider.regression(linear_regression_model)

print(f'Model 1: {linear_regression_model.get_model_informations()}')


stats = StatisticalAnalyzer.analyze(y1)
print(stats)
entropy: float = StatisticalAnalyzer.calculate_entropy(y1)
print(f"Entropia {entropy}")

rel_freq_result: RelfreqResult = StatisticalAnalyzer.relative_frequency(y1, 25, True)
cum_freq_result: CumfreqResult = StatisticalAnalyzer.cumulated_frequency(y1, 25, True)

print(f"Relative frequency: {rel_freq_result}")
print(f"Cumulated frequency: {cum_freq_result}")

plt.show()