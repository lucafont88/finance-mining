
from typing import Dict, List, Union
import datetime

class Axis:

    def __init__(self, label: str, x: List[Union[int, float, datetime.datetime]], y: List[Union[int, float]]):
        self.label = label
        self.x = x
        self.y = y

class PlotModel:

    title: str
    x_label: str
    y_label: str
    data: Dict[int, Axis] = {}

    def __init__(self, title: str, x_label: str, y_label: str, axis_list: List[Axis] = []):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        counter: int = 0
        if axis_list is not None:
            for axis in axis_list:
                self.data[counter] = axis
                counter += 1
