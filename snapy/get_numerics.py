"""Numerics analysis functions."""

# %% External package import

from numpy import delete, dot, empty, fft
from pandas import DataFrame, Series

# %% Function definitions


def compute_discrete_fourier(data):
    """
    Calculate the discrete fourier transform over the data.

    Parameters
    ----------
    data : Dataframe
        Pandas dataframe with the column for which to calculate the \
        discrete fourier transform.

    Returns
    -------
    sp : ndarray
        Array with the signal peak values.

    freq : ndarray
        Array with the frequency values.
    """

    # Check if the data is either a series or a dataframe with one column
    if isinstance(data, Series) or isinstance(data, DataFrame) and data.shape[1] == 1:
        # Get the signal peaks
        sp = fft.fft(data)

        # Get the frequencies
        freq = fft.fftfreq(data.shape[-1])

        return sp, freq

    else:
        # Raise an index error to indicate a too high number of columns
        raise IndexError("Too many columns passed, only one column allowed!")


def compute_acf(data, drop_cols=None):
    """
    Compute the autocorrelation function .

    Parameters
    ----------
    data : ndarray
        Array with the data values.

    drop_cols : iterable
        Iterable with the columns to drop from the array.

    Returns
    -------
    float
        Value of the autocorrelation.
    """

    # Check if data columns should be dropped
    if drop_cols:
        # Loop over the columns to drop
        for col in drop_cols:
            # Delete the column
            data = delete(data, col, 1)

    # Initialize the result array
    result = empty((data.shape[0], int(data.shape[1] / 2)), dtype=complex)

    # Set the real part of the values
    result.real = data[:, ::2]

    # Set the imaginary part of the values
    result.imag = data[:, 1::2]

    # Calculate the ACF
    acf = sum(dot(result[:, 0], result[:, i]) for i in range(result[:,].shape[0]))

    return acf
