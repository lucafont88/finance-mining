from sklearn import preprocessing
import numpy as np

class SimplePreprocessEngine:

    @staticmethod
    def standard_scaler(train_data: np.array):
        scaler = preprocessing.StandardScaler().fit(train_data)
        data_transformed = scaler.transform(train_data)
        return data_transformed