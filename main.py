from libs.configuration.configuration_reader import ConfigurationReader
from libs.security.secret_manager import SecretManager
from libs.analyzer.engines.linear_analyzer_engine import LinearAnalyzerEngine

# import streamlit as st

# st.title('FinFetch Analyzer')

SECRET_FILE = './secrets.txt'
CONFIG_FILE = './config.config'
PROMPT_DEBUG = False
secret_manager = SecretManager(SECRET_FILE)
secret_manager.read_secrets_file()
configuration_reader = ConfigurationReader(CONFIG_FILE)
configuration_reader.read_configuration_file()
linear_analyzer_engine = LinearAnalyzerEngine(secret_manager, configuration_reader, PROMPT_DEBUG)
CSV_TO_LOAD_FILE = configuration_reader.get_secret(configuration_reader.CSV_TO_LOAD_FILE_TOKEN)
stats, rel_freq_result, cum_freq_result, model_info, poly_models, plot_model = linear_analyzer_engine.run(CSV_TO_LOAD_FILE, 'high')

print('End!')