import matplotlib.pyplot as plt
from libs.plotting.plot_model import PlotModel

class PlotEngine:

    def __init__(self):
        pass

    def plot(self, plot_model: PlotModel):
        # Plotting
        fig, axs = plt.subplots()  # Create a figure and an axes.
        axs.plot(list(plot_model.x1), list(plot_model.y1), label=plot_model.label1)
        axs.plot(list(plot_model.x2), list(plot_model.y2), label=plot_model.label2)
        axs.set_xlabel(plot_model.x_label)  # Add an x-label to the axes.
        axs.set_ylabel(plot_model.y_label)  # Add a y-label to the axes.
        axs.set_title(plot_model.title)  # Add a title to the axes.
        axs.legend()  # Add a legend.
        plt.show()