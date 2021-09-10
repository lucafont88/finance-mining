from libs.analyzer.regressions.linear_regression import LinearRegression
from libs.plotting.plot_engine import PlotEngine
from libs.plotting.plot_model import PlotModel
from typing import List
from libs.data_loader.file_to_load_reader import FileToLoadReader
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from libs.utility.secret_manager import SecretManager
from libs.data_loader.data_loader import DataLoader

SECRET_FILE = './secrets.txt'
CSV_TO_LOAD_FILE = './resourse_to_load.txt'
secret_manager = SecretManager(SECRET_FILE)
repository_url: str = secret_manager.read_secrets_file()
print(f"Repository URL: {repository_url}")
print("---------------------------------")
data_loader = DataLoader(secret_manager.get_csv_repository_url())
file_to_load_reader = FileToLoadReader(CSV_TO_LOAD_FILE)
csv_files: List[str] = file_to_load_reader.read_file()
for csv_file in csv_files:
    print(f"Csv to load: {csv_file}")
print("---------------------------------")

data: List[pd.DataFrame] = data_loader.load_data(csv_files)

# i = 1
# for data_frame in data:
#     print(f'Data Frame {i}:')
#     print(data_frame.head())
#     i += 1

intraday: pd.DataFrame = data[0]
daily: pd.DataFrame = data[1]

x1 = list(intraday['index'])
y1 = list(intraday['high'])
label1 = 'High'
x2 = list(intraday['index'])
y2 = list(intraday['low'])
label2 = 'Low'

plot_model = PlotModel('EurUsd daily 1min', 'tick', 'price', x1, y1, label1, x2, y2, label2)
plot_engine = PlotEngine()
plot_engine.plot(plot_model)


linear_regression_model_1 = LinearRegression(x1, y1)
linear_regression_model_1.train()
linear_regression_model_1.plot_model(title = 'Linear Regression Model 1')

linear_regression_model_2 = LinearRegression(x2, y2)
linear_regression_model_2.train()
linear_regression_model_2.plot_model(title = 'Linear Regression Model 2')

model_1_info = linear_regression_model_1.get_model_informations()
model_2_info = linear_regression_model_2.get_model_informations()

print(f'Model 1: {model_1_info}')
print(f'Model 2: {model_2_info}')

plt.show()