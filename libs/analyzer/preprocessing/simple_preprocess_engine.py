from sklearn import preprocessing
import numpy as np

class SimplePreprocessEngine:

    @staticmethod
    def standard_scaler(train_data: np.array):
        """
        Standardize features by removing the mean and scaling to unit variance
        The standard score of a sample x is calculated as:
        z = (x - u) / s
        where u is the mean of the training samples and s is the standard deviation of the training samples.

        :param train_data:

        :return: Standardized train data
        """
        scaler = preprocessing.StandardScaler().fit(train_data)
        data_transformed = scaler.transform(train_data)
        return data_transformed

    @staticmethod
    def min_max_scaler(train_data: np.array, min: float = 0, max: float = 1):
        """
        Transform features by scaling each feature to a given range.

        :param train_data: Train data
        :param min: Minimum value
        :param max: Maximum value

        :return: Min-Max scaled train data
        """
        scaler = preprocessing.MinMaxScaler(feature_range=(min, max)).fit(train_data)
        data_transformed = scaler.transform(train_data)
        return data_transformed

    @staticmethod
    def maximum_absolute_scaler(train_data: np.array):
        """
        Scale each feature by its maximum absolute value. It does not shift the data, just scale.

        :param train_data: Train data

        :return: Max absolute scaled train data
        """
        scaler = preprocessing.MaxAbsScaler().fit(train_data)
        data_transformed = scaler.transform(train_data)
        return data_transformed