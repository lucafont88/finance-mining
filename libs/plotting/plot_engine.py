import matplotlib.pyplot as plt
from libs.plotting.plot_model import PlotModel

class PlotEngine:

    def plot(self, plot_model: PlotModel):
        # Plotting
        fig, axs = plt.subplots()  # Create a figure and an axes.
        for model in plot_model.data.values():
            axs.plot(list(model.x), list(model.y), label=model.label)
        axs.set_xlabel(plot_model.x_label)  # Add an x-label to the axes.
        axs.set_ylabel(plot_model.y_label)  # Add a y-label to the axes.
        axs.set_title(plot_model.title)  # Add a title to the axes.
        axs.legend()  # Add a legend.

    def get_figure(self, plot_model: PlotModel) -> plt.Figure:
        fig, axs = plt.subplots()  # Create a figure and an axes.
        for model in plot_model.data.values():
            axs.plot(list(model.x), list(model.y), label=model.label)
            axs.set_xlabel(plot_model.x_label)  # Add an x-label to the axes.
            axs.set_ylabel(plot_model.y_label)  # Add a y-label to the axes.
            axs.set_title(plot_model.title)  # Add a title to the axes.
            axs.legend()  # Add a legend.
        return fig