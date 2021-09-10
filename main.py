from typing import List
from libs.data_loader.file_to_load_reader import FileToLoadReader
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
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

i = 1
for data_frame in data:
    print(f'Data Frame {i}:')
    print(data_frame.head())
    i += 1