import seaborn
import matplotlib.pyplot as plt
import numpy as np


def pairplot(data, savefile=None):
    """
    Create a pair plot from input data and either show it or save it
    :param data: Data in the format that is capable of being pairplotted
    :param savefile: If True saving takes place, if False only visualization.
     Arg is the filepath
    :return:
    """
    # Create a pairplot
    seaborn.pairplot(data=data, height=1.05, aspect=2)
    if savefile is None:
        plt.show()
    else:
        # Save the plot as a .pdf
        plt.savefig(savefile, format="pdf")
        plt.close()


def barplot(data, labels, savefile=None):
    """
    Create a pair plot from input data and either show it or save it
    :param data: array(columns) List of data points in the format
    that is capable of being bar plotted
    :param labels: List of names of bar labels
    :param savefile: If True saving takes place, if False only visualization.
     Arg is the filepath
    :return:
    """
    # Create a bar plot
    plt.figure(figsize=(20, 20))
    plt.bar(
        np.arange(0, len(data)),
        np.array(data),
        tick_label=labels,
    )
    if savefile is None:
        plt.show()
    else:
        # Save the plot as a .pdf
        plt.savefig(savefile, format="pdf")
        plt.close()


def simple_plot(data, savefile=None):
    """
    Create a simple plot from input data and either show it or save it
    :param data: array(x, y)
    :param savefile: If True saving takes place, if False only visualization.
     Arg is the filepath
    :return:
    """

    # Open a figure
    plt.figure(figsize=(20, 10))

    # Create a line plot with the real frequencies
    plt.plot(data[0], data[1])

    plt.xlabel("Frequency", fontsize=12)
    if savefile is None:
        plt.show()
    else:
        # Save the plot as a .pdf
        plt.savefig(savefile, format="pdf")
        plt.close()
