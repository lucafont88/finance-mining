from typing import List
import pandas as pd
class DataLoader:

    def __init__(self):
        pass

    def load_data_from_url(self, url) -> List[pd.DataFrame]:
        self.__validate_csv_url(url)
        return pd.read_csv(url)

    def load_data(self, url_list: List[str]):
        df_list: List[pd.DataFrame] = []
        for url in url_list:
            df = self.load_data_from_url(url)
            df_list.append(df)
        return df_list

    def __validate_csv_url(self, url):
        if url is None:
            raise ValueError("url is None")
        if url.endswith(".csv") is False:
            raise ValueError("url is not csv")