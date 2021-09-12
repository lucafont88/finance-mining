
from typing import List, Union
import datetime

class AnalysisModel:

    name: str
    X: List[Union[float, int, datetime.datetime]]
    Y: List[Union[float, int]]

    def __init__(self, name: str, X: List[Union[float, int, datetime.datetime]], Y: List[Union[float, int]]):
        self.name = name
        self.X = X
        self.Y = Y