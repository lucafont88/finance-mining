
import json
from libs.utility.numpy_encoder import NumpyEncoder

class FileSaver:
    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, text: str):
        with open(self.file_path, 'w') as file:
            file.write(text)

    def save_json(self, data: dict):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4, cls=NumpyEncoder)