import numpy as np

def merge_dicts(dict1: dict, dict2: dict) -> dict:
    """
    Merges two dictionaries into one.
    """
    return {**dict1, **dict2}

def get_numpy_2d_array(x: list, y: list) -> np.ndarray:
    """
    Converts a list of lists to a numpy array.
    """
    return np.array(list(zip(x, y)))