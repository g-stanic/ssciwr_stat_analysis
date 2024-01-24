import os

import seaborn
import matplotlib.pyplot as plt
import numpy as np


def pairplot(data, path, filename: str, save=False):
    """
    Create a pair plot from input data and either show it or save it
    :param data: Data in the format that is capable of being pairplotted
    :param path: Path where the file will be saved
    :param filename: Name of the saved file
    :param save: If True saving takes place, if False only visualization
    :return:
    """
    # Create a pairplot
    seaborn.pairplot(data=data, height=1.05, aspect=2)
    if save:
        # Save the plot as a .pdf
        plt.savefig(os.path.join(path, filename + ".pdf"), format="pdf")
        plt.close()
    else:
        plt.show()


def barplot(data, labels, path, filename: str, save=False):
    """
    Create a pair plot from input data and either show it or save it
    :param data: array(columns) List of data points in the format
    that is capable of being bar plotted
    :param labels: List of names of bar labels
    :param path: Path where the file will be saved
    :param filename: Name of the saved file
    :param save: If True saving takes place, if False only visualization
    :return:
    """
    # Create a bar plot
    plt.figure(figsize=(20, 20))
    plt.bar(
        np.arange(0, len(data)),
        np.array(data),
        tick_label=labels,
    )
    plt.title(f"{filename}")
    if save:
        # Save the plot as a .pdf
        plt.savefig(os.path.join(path, filename + ".pdf"), format="pdf")
        plt.close()
    else:
        plt.show()


def simple_plot(data, path, filename: str, save=False):
    """
    Create a simple plot from input data and either show it or save it
    :param data: array(x, y)
    :param path: Path where the file will be saved
    :param filename: Name of the saved file
    :param save: If True saving takes place, if False only visualization
    :return:
    """

    # Open a figure
    plt.figure(figsize=(20, 10))

    # Create a line plot with the real frequencies
    plt.plot(data[0], data[1])

    # Plot styling
    plt.title(f"{filename}", fontsize=18)
    # plt.xlabel("Frequency", fontsize=12)
    if save:
        # Save the plot to a .pdf
        plt.savefig(os.path.join(path, filename + ".pdf"), format="pdf")
        plt.close()
    else:
        plt.show()
