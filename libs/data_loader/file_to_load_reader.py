
from typing import Iterable, List


class FileToLoadReader:

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def read_file(self) -> Iterable[str]:
        with open(self._file_path, 'r') as file:
            return file.readlines()