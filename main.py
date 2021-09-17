from libs.configuration.configuration_reader import ConfigurationReader
from libs.security.secret_manager import SecretManager
from libs.analyzer.engines.linear_analyzer_engine import LinearAnalyzerEngine

SECRET_FILE = './secrets.txt'
CONFIG_FILE = './config.config'
CSV_TO_LOAD_FILE = './resourse_to_load.txt'
PROMPT_DEBUG = False
secret_manager = SecretManager(SECRET_FILE)
secret_manager.read_secrets_file()
configuration_reader = ConfigurationReader(CONFIG_FILE)
configuration_reader.read_configuration_file()
linear_analyzer_engine = LinearAnalyzerEngine(secret_manager, configuration_reader, PROMPT_DEBUG)
linear_analyzer_engine.run(CSV_TO_LOAD_FILE)

print('End!')