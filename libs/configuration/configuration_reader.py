from typing import Dict, List, Union

class ConfigurationReader:
    """
    After calling the constructor, you must call the read_configuration_file method in order collect settings
    """
    INTERPOLATION_DEGREES_TOKEN: str = 'INTERPOLATION_DEGREES'
    INTERPOLATION_N_POINTS_TOKEN: str = 'INTERPOLATION_N_POINTS'
    CSV_TO_LOAD_FILE_TOKEN: str = 'CSV_TO_LOAD_FILE'
    OUTPUT_FILE_TOKEN: str = 'OUTPUT_FILE'

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
        return self.__get_value(secret_key)

    def get_interpolation_degree_list(self) -> List[int]:
        """
        Returns the connection string for MongoDB

        :return: The connection string
        """
        interpolation_degrees_str = self.__get_value(self.INTERPOLATION_DEGREES_TOKEN)
        interolation_degrees: List[str] = interpolation_degrees_str.replace("[", "").replace("]", "").split(',')
        interolation_degrees_list: List[int] = [int(degree) for degree in interolation_degrees]
        return interolation_degrees_list

    def get_interpolation_n_samples(self) -> int:
        return int(self.__get_value(self.INTERPOLATION_N_POINTS_TOKEN))

    # Private methods
    def __get_value(self, secret_key: str) -> str:
        """
        Return the secret value for the given key

        :param secret_key: The key of the secret

        :return: The secret value
        """
        return self.configurations[secret_key]