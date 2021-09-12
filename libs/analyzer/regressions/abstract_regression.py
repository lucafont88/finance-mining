import uuid
from abc import ABC, abstractmethod
from typing import List

class AbstractRegression(ABC):
    def __init__(self):
        self.__id: str = str(uuid.uuid4())

    def get_id(self) -> str:
        return self.__id

    @abstractmethod
    def set_x(self, x: List[float]) -> None:
        pass

    @abstractmethod
    def set_y(self, y: List[float]) -> None:
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self, x: float) -> float:
        pass

    @abstractmethod
    def get_model(self):
        pass

    @abstractmethod
    def get_model_informations(self) -> dict:
        pass

    @abstractmethod
    def plot_model(self, *args, **kwargs):
        pass