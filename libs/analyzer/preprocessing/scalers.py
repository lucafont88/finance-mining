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

    @staticmethod
    def robust_outlier_scaler(train_data: np.array):
        """
        Scale features using statistics that are robust to outliers.
        This Scaler removes the median and scales the data according to the quantile range (defaults to IQR: Interquartile Range). 
        The IQR is the range between the 1st quartile (25th quantile) and the 3rd quartile (75th quantile).
        Centering and scaling happen independently on each feature by computing the relevant statistics on the samples 
        in the training set.

        :param train_data: Train data

        :return: Robust outlier scaled train data
        """
        scaler = preprocessing.RobustScaler().fit(train_data)
        data_transformed = scaler.transform(train_data)
        return data_transformed

    @staticmethod
    def normalize(train_data: np.array, chosen_norm: str = 'l2'):
        """
        Normalization is the process of scaling individual samples to have unit norm. 
        This process can be useful if you plan to use a quadratic form such as the dot-product 
        or any other kernel to quantify the similarity of any pair of samples.

        :param train_data: Train data
        :param norm: The norm to use to normalize each non zero sample (or each non-zero feature if axis is 0). {‘l1’, ‘l2’, ‘max’}, default=’l2’

        :return: Normalized train data
        """
        return preprocessing.normalize(train_data, chosen_norm)