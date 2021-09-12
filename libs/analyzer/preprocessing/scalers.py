from typing import Literal, Union
from sklearn import preprocessing
import numpy as np

class ScalerModel:
    scaler_type: str
    min_value: Union[int, float]
    max_value: Union[int, float]
    norm: Literal['l1', 'l2', 'max']

    def __init__(self, scaler_type: str, min_value: Union[int, float] = None, max_value: Union[int, float] = None, norm: Literal['l1', 'l2', 'max'] = None) -> None:
        self.scaler_type = scaler_type
        self.min_value = min_value
        self.max_value = max_value
        self.norm = norm

def apply_scaler(train_data: np.array, scaler_model: ScalerModel = None) -> np.array:
    """
    Applies a scaler to a given dataset.
    :param scaler_model: ScalerModel object

    :return scaled data
    """
    if scaler_model is None:
        return train_data

    if scaler_model.scaler_type is None or scaler_model.scaler_type == '':
        raise ValueError('Scaler type not specified.')
    
    scaler_type = scaler_model.scaler_type.lower()

    train_data = np.array(train_data).reshape(-1, 1)

    if scaler_type == 'standard_scaler':
        return PreprocessScalers.standard_scaler(train_data)
    elif scaler_type == 'min_max_scaler':
        if scaler_model.min_value is None or scaler_model.max_value is None:
            raise ValueError('Min and max values not specified.')
        return PreprocessScalers.min_max_scaler(train_data, scaler_model.min_value, scaler_model.max_value)
    elif scaler_type == 'maximum_absolute_scaler':
        return PreprocessScalers.maximum_absolute_scaler(train_data)
    elif scaler_type == 'robust_outlier_scaler':
        PreprocessScalers.robust_outlier_scaler(train_data)
    elif scaler_type == 'normalizer':
        if scaler_model.norm is None or scaler_model.norm == '':
            raise ValueError('Norm not specified.')
        return PreprocessScalers.normalize(train_data, scaler_model.norm)
    else:
        raise ValueError('Scaler type not recognized.')

class PreprocessScalers:

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