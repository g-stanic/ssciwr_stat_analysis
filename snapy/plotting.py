import seaborn
import matplotlib.pyplot as plt
import numpy as np


def pairplot(data, savefile=None):
    """
    Create a pair plot from input data and either show it or save it

    Parameters
    ----------
    data : Dataframe
        Data in the format that is capable of being pair-plotted.

    savefile : string or None
        If string saving takes place, if None only visualization.
        The argument is supposed to be a filepath together with the filename.

    Returns
    -------
    Plots or saves the graph based on the savefile argument
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

    Parameters
    -------
    data : array(columns)
        List of data points in the format that is capable of being bar plotted

    labels : array
        List of names of bar labels

    savefile : string or None
        If string saving takes place, if None only visualization.
        The argument is supposed to be a filepath together with the filename.

    Returns
    -------
    Plots or saves the graph based on the savefile argument
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

    Parameters
    -------
    data : array(x, y)

    savefile : string or None
        If string saving takes place, if None only visualization.
        The argument is supposed to be a filepath together with the filename.

    Returns
    -------
    Plots or saves the graph based on the savefile argument
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
