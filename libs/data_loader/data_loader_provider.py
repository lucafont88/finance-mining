
from libs.data_loader.file_to_load_reader import FileToLoadReader
from libs.data_loader.data_loader import DataLoader
from typing import List
import pandas as pd
from libs.utility.secret_manager import SecretManager


class DataLoaderProvider:

    def __init__(self, secret_file_path: str, csv_to_fetch_file_path: str) -> None:
        self.__secret_manager = SecretManager(secret_file_path)
        self.csv_to_fetch_file_path = csv_to_fetch_file_path

    def load_data(self, prompt_debug_info: bool = True) -> List[pd.DataFrame]:
        repository_url: str = self.__secret_manager.read_secrets_file()
        
        # For debugging purposes
        if prompt_debug_info is True:
            print(f"Repository URL: {repository_url}")
            print("---------------------------------")
            
        data_loader = DataLoader(self.__secret_manager.get_csv_repository_url())
        file_to_load_reader = FileToLoadReader(self.csv_to_fetch_file_path)
        csv_files: List[str] = file_to_load_reader.read_file()

        # For debugging purposes
        if prompt_debug_info is True:
            for csv_file in csv_files:
                print(f"Csv to load: {csv_file}")
            print("---------------------------------")

        return data_loader.load_data(csv_files)     