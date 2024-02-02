import sys

import snapy_io as io
import get_statistics as stat
import plotting as plot

# Stasticial tasks


def plot_data_simple(data_file, plot_outfile=""):
    """
    Reads in data from data file and create a relevant plot.

    Parameters
    ----------
    data_file : str
        Path to data file.

    plot_outfile : str
        File where plot will be saved.
        If plot_outfile = "" plot will only be displayed and not saved.
    """

    data = io.read_as_df(data_file)

    if data is None:
        # function prints error message if file doesn't exist so just exit
        sys.exit("File Error")
    else:
        plot.simple_plot(data, plot_outfile)


# Calculate correlation coefficients, flags for drop var, make plot, save output
def calculate_correlation_coefficnes(
    data_file,
    text_outfile,
    var_tolerance=None,
    method="pearson",
    drop_cols=None,
    return_sorted=True,
    plot_outfile="",
):
    """
    Reads in data from data file, calculates the correlation coefficients,
    can output the coefficients to a text file,
    and save a pair plot of all the variables.

    Parameters
    ----------
    data_file : str
        Path to data file.
        method : string, default='pearson'
        Correlation method as a string.

    text_outfile : File where correlation coefficients will be saved.

    var_tolerance : None or float
        Calculate correlation coefficients only for columms
        which have variance above this threshold.
        If var_tolerance == None then no test for variance will be done.

    drop_cols : iterable, default=None
        Iterable with data columns to drop before correlating.

    return_sorted : bool, default=True
        Indicator for sorting the output by absolute correlation value.

    plot_file : str
        File where plot will be saved.
        If plot_file = "" plot will only be displayed and not saved.
    """

    data = io.read_as_df(data_file)

    if data is None:
        # function prints error message if file doesn't exist so just exit
        sys.exit("File Error")
    else:
        coeffs = stat.correlate(
            data, method=method, drop_cols=drop_cols, return_sorted=return_sorted
        )
        print(coeffs)


# Calculate Euclidean distance, flags for clean data, make plot, save output

# Numerical tasks

# Fourier-transform, flags for drop var, make plot,

# Autocorrelaiton function, flags for clean data, make plot
