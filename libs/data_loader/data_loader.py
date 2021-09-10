from typing import List
import pandas as pd
class DataLoader:

    def __init__(self, base_url: str):
        self._base_url = base_url

    def load_data_from_url(self, csv_name) -> pd.DataFrame:
        if csv_name is None:
            raise ValueError("csv_name is None")
        if csv_name.endswith(".csv") is False:
            csv_name += ".csv"
        resource: str = '/'.join([self._base_url, csv_name])
        self.__validate_csv_url(resource)
        return pd.read_csv(resource)

    def load_data(self, csv_names: List[str]) -> List[pd.DataFrame]:
        df_list: List[pd.DataFrame] = []
        for csv_name in csv_names:
            csv_name = csv_name.strip()
            df = self.load_data_from_url(csv_name)
            df_list.append(df)
        return df_list

    def __validate_csv_url(self, url):
        if url is None:
            raise ValueError("url is None")
        if url.endswith(".csv") is False:
            raise ValueError("url is not csv")