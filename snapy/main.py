# import os
import sys

import snapy_io as io

# import get_statistics as stat

# Stasticial tasks

# Read in data and make basic plots, needs flag for drop var


def plot_basic_data(data_file, plot_file):
    """
    Reads in data from data file and create a relevant plot.

    Parameters
    ----------
    data_file : Path to data file to be plotted."""

    data = io.read_as_df(data_file)

    if data is None:
        # function prints error message if file doesn't exist so just exit
        sys.exit("File Error")
    # else:
    # plot_data


# Calculate correlation coefficients, flags for drop var, make plot, save output

# Calculate Euclidean distance, flags for clean data, make plot, save output

# Numerical tasks

# Fourier-transform, flags for drop var, make plot,

# Autocorrelaiton function, flags for clean data, make plot
