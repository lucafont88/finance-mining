from scipy import stats
from scipy.stats.stats import CumfreqResult, DescribeResult, RelfreqResult, cumfreq
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
        else:
            cumfreq = stats.cumfreq(data, numbins=num_bins)
            x = cumfreq.lowerlimit + np.linspace(0, cumfreq.binsize * cumfreq.cumcount.size,
                                 cumfreq.cumcount.size)
            fig = plt.figure(figsize=(10, 4))
            ax1 = fig.add_subplot(1, 2, 1)
            ax2 = fig.add_subplot(1, 2, 2)
            ax1.hist(cumfreq, bins=num_bins)
            ax1.set_title('Histogram')
            ax2.bar(x, cumfreq.cumcount, width=cumfreq.binsize)
            ax2.set_title('Cumulative histogram')
            ax2.set_xlim([x.min(), x.max()])

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
            rel_freq = stats.relfreq(data, numbins=num_bins)
            x = rel_freq.lowerlimit + np.linspace(0, rel_freq.binsize * rel_freq.frequency.size,
                                 rel_freq.frequency.size)
            fig = plt.figure(figsize=(5, 4))
            ax = fig.add_subplot(1, 1, 1)
            ax.bar(x, rel_freq.frequency, width=rel_freq.binsize)
            ax.set_title('Relative frequency histogram')
            ax.set_xlim([x.min(), x.max()])

    # def probability_density_function(data):
    #     """
    #     This method is used to analyze the probability density function.
    #     :param data: The data to analyze.
    #     :return: The result of the analysis.
    #     """
    #     return stats.kde.gaussian_kde(data)