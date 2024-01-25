import numpy as np
import pandas as pd
import os

# Functions which deal with input of data


def check_exists(file):
    ierr = 0
    if not os.path.exists(file):
        print("Error file does not exist: {}".format(file))
        ierr = 1
    return ierr


def read_as_df(file):
    """Reads in the given file and returns it as a pandas dataframe.
    This function assumes that data in the file is seperated with whitespace.
    Returns: df (pandas DataFrame, returned as None if file does not exist.)"""
    ierr = check_exists(file)

    if ierr == 0:  # file exists
        df = pd.read_csv(file, sep="\s+")  # noqa
    else:  # file does not exit
        df = None
    return df


def drop_low_variance_df(df, var_threshold):
    """Drop columns from the data frame with variance below a threshold.
    Returns: df (dataframe with columns dropped)"""

    # Get the columns to drop
    columns_to_drop = [col for col in df.columns if df.var()[col] < var_threshold]

    # Print a message about the columns to drop
    print(
        """These columns will be discarded as their
        variance is below the set threshold""",
        columns_to_drop,
    )

    # Drop the columns from the data frame
    df.drop(columns=columns_to_drop, inplace=True)

    return df


def read_as_array(file, names=None, skip_header=0):
    """Reads in the given file and returns in as a numpy array.
    Arguments names and skip_header behave as in the function numpy.genfromtxt.
    Returns: array (numpy array, returned as None if file does not exist.)"""
    ierr = check_exists(file)
    if ierr == 0:  # file exists
        array = np.genfromtxt(file, names=names, skip_header=skip_header)
    else:  # file does not exist
        array = None
    return array


def clean_nans(array):
    """Replaces nans in the array with zeros.
    Returns: array"""
    clean_array = np.nan_to_num(array)
    return clean_array


# Functions which deal with text output of data


def save_df(df, output_file, header=True, index=False):
    """Saves the data frame to the output file.
    Arguments header and index have the same usage as pandas.to_csv"""
    df.to_csv(output_file, sep="\t", header=header, index=index)


def save_array(array, output_file, header=""):
    """Saves the array to the output file.
    Argument header has the same usage as numpy.savetxt"""
    np.savetxt(output_file, array, header=header)
