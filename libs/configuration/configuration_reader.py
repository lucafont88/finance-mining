from typing import Dict, Union

class ConfigurationReader:
    """
    After calling the constructor, you must call the read_configuration_file method in order collect settings
    """

    def __init__(self, configuration_file: str):
        """
        Initialize the secret manager

        :param configuration_file: The path to the configuration file
        """
        self.configuration_file = configuration_file
        self.configurations = {}

    def read_configuration_file(self) -> None:
        """
        Get the configurations from the configurations file
        Must be called before tryig to get configurations
        """
        with open(self.configuration_file, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                line_splitted = line.split('=')
                if len(line_splitted) == 2:
                    self.configurations[line_splitted[0].strip()] = line_splitted[1].strip()
                elif len(line_splitted) < 2:
                    raise ValueError('Configuration file is not valid')
                else:
                    value = '='.join([s.strip() for s in line_splitted[1:]])
                    self.configurations[line_splitted[0].strip()] = value
                

    def get_secret(self, secret_key: str) -> str:
        """
        Return the secret value for the given key

        :param secret_key: The key of the secret

        :return: The secret value
        """
        return self.__get_secret(secret_key)

    def get_mongo_connection_string(self) -> str:
        """
        Returns the connection string for MongoDB

        :return: The connection string
        """
        return self.__get_secret(self.ATLAS_MONGO_DB_CONNECTION_STRING_TOKEN)

    # Private methods
    def __get_secret(self, secret_key: str) -> str:
        """
        Return the secret value for the given key

        :param secret_key: The key of the secret

        :return: The secret value
        """
        return self.secrets[secret_key]