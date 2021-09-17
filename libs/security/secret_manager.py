from typing import Dict, Union

class SecretManager:
    """
    After calling the constructor, you must call the read_secrets_file method in order to fill the dictionary with secrets
    """

    FINFETCH_CSV_REPOSITORY_URL_TOKEN: str = 'FINFETCH_CSV_REPOSITORY_URL'

    def __init__(self, secret_file: str):
        """
        Initialize the secret manager

        :param secret_file: The path to the secrets file
        """
        self.secret_file = secret_file
        self.secrets = {}

    def read_secrets_file(self) -> None:
        """
        Get the secrets from the secrets file
        Must be called before tryig to get secrets
        """
        with open(self.secret_file, 'r') as reader:
            lines = reader.readlines()
            for line in lines:
                line_splitted = line.split('=')
                if len(line_splitted) == 2:
                    self.secrets[line_splitted[0].strip()] = line_splitted[1].strip()
                elif len(line_splitted) < 2:
                    raise ValueError('Secrets file is not valid')
                else:
                    value = '='.join([s.strip() for s in line_splitted[1:]])
                    self.secrets[line_splitted[0].strip()] = value
                

    def get_secret(self, secret_key: str) -> str:
        """
        Return the secret value for the given key

        :param secret_key: The key of the secret

        :return: The secret value
        """
        return self.__get_secret(secret_key)

    def get_csv_repository_url(self) -> str:
        """
        Return the csv repository url

        :return: The csv repository url
        """
        return self.__get_secret(self.FINFETCH_CSV_REPOSITORY_URL_TOKEN)

    # Private methods
    def __get_secret(self, secret_key: str) -> str:
        """
        Return the secret value for the given key

        :param secret_key: The key of the secret

        :return: The secret value
        """
        return self.secrets[secret_key]