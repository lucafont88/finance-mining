from libs.plotting.plot_model import PlotModel
from typing import Any, Dict, Union

from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult
from sklearn.pipeline import Pipeline
from libs.configuration.configuration_reader import ConfigurationReader
from libs.security.secret_manager import SecretManager
from libs.analyzer.engines.linear_analyzer_engine import LinearAnalyzerEngine

class FinanceMiningService:
    
    def __init__(self, prompt_debug: bool):
        SECRET_FILE = './secrets.txt'
        CONFIG_FILE = './config.config'
        self.__secret_manager = SecretManager(SECRET_FILE)
        self.__configuration_reader = ConfigurationReader(CONFIG_FILE)
        self.__PROMPT_DEBUG = prompt_debug
    
    def run(self) -> Union[DescribeResult, RelfreqResult, CumfreqResult, Dict[str, Any], Dict[int, Pipeline], PlotModel]:
        self.__secret_manager.read_secrets_file()
        self.__configuration_reader.read_configuration_file()
        CSV_TO_LOAD_FILE = self.__configuration_reader.get_secret(self.__configuration_reader.CSV_TO_LOAD_FILE_TOKEN)
        linear_analyzer_engine = LinearAnalyzerEngine(self.__secret_manager, self.__configuration_reader, self.__PROMPT_DEBUG)
        return linear_analyzer_engine.run(CSV_TO_LOAD_FILE, 'high')

