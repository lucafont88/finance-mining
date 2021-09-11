from scipy import stats

class StatisticalAnalyzer:
    """
    This class is used to analyze the statistical data.
    """

    @staticmethod
    def analyze(data):
        """
        This method is used to analyze the statistical data.
        :param data: The data to analyze.
        :return: The result of the analysis.
        """
        return stats.describe(data)

    @staticmethod
    def calculate_entropy(data) -> float:
        """
        This method is used to calculate the entropy of the data.
        :param data: The data to calculate the entropy.
        :return: The entropy of the data.
        """
        return stats.entropy(data)

    @staticmethod
    def cumulated_frequency(data, num_bins: int) -> list:
        """
        This method is used to calculate the cumulated frequency of the data.
        :param data: The data to calculate the cumulated frequency.
        :param num_bins: The number of bins to use.

        :return: The cumulated frequency of the data.
        """
        return stats.cumfreq(data, numbins=num_bins)

    @staticmethod
    def relative_frequency(data, num_bins: int) -> list:
        """
        This method is used to calculate the relative frequency of the data.
        :param data: The data to calculate the relative frequency.
        :param num_bins: The number of bins to use.
        
        :return: The relative frequency of the data.
        """
        return stats.relfreq(data, numbins=num_bins)

    def probability_density_function(data):
        """
        This method is used to analyze the probability density function.
        :param data: The data to analyze.
        :return: The result of the analysis.
        """
        return stats.kde.gaussian_kde(data)