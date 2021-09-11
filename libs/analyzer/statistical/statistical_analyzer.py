from scipy import stats
from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult
import matplotlib.pyplot as plt
import numpy as np

class StatisticalAnalyzer:
    """
    This class is used to analyze the statistical data.
    """

    @staticmethod
    def analyze(data) -> DescribeResult:
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
    def cumulated_frequency(data, num_bins: int, show_plot: bool = True) -> CumfreqResult:
        """
        This method is used to calculate the cumulated frequency of the data.
        :param data: The data to calculate the cumulated frequency.
        :param num_bins: The number of bins to use.

        :return: The cumulated frequency of the data.
        """
        if show_plot is False:
            return stats.cumfreq(data, numbins=num_bins)
        # else:
        #     cumfreq_result = stats.cumfreq(data, numbins=num_bins)
        #     x = cumfreq_result.lowerlimit + np.linspace(0, cumfreq_result.binsize * cumfreq_result.frequency.size,
        #                          cumfreq_result.frequency.size)
        #     fig = plt.figure(figsize=(5, 4))
        #     ax = fig.add_subplot(1, 1, 1)
        #     ax.bar(x, cumfreq_result.frequency, width=cumfreq_result.binsize)
        #     ax.set_title('Relative frequency histogram')
        #     ax.set_xlim([x.min(), x.max()])

    @staticmethod
    def relative_frequency(data, num_bins: int, show_plot: bool = True) -> RelfreqResult:
        """
        This method is used to calculate the relative frequency of the data.
        :param data: The data to calculate the relative frequency.
        :param num_bins: The number of bins to use.

        :return: The relative frequency of the data.
        """
        if show_plot is False:
            return stats.relfreq(data, numbins=num_bins)
        else:
            cumfreq_result = stats.relfreq(data, numbins=num_bins)
            x = cumfreq_result.lowerlimit + np.linspace(0, cumfreq_result.binsize * cumfreq_result.frequency.size,
                                 cumfreq_result.frequency.size)
            fig = plt.figure(figsize=(5, 4))
            ax = fig.add_subplot(1, 1, 1)
            ax.bar(x, cumfreq_result.frequency, width=cumfreq_result.binsize)
            ax.set_title('Relative frequency histogram')
            ax.set_xlim([x.min(), x.max()])

    # def probability_density_function(data):
    #     """
    #     This method is used to analyze the probability density function.
    #     :param data: The data to analyze.
    #     :return: The result of the analysis.
    #     """
    #     return stats.kde.gaussian_kde(data)