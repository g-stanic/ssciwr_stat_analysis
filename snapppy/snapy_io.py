import numpy as np
import pandas as pd
import os

# Functions which deal with input of data


def check_exists(file):
    """
    Checks that a file exists. Prints an error but does not exit.

    Parameters
    ----------
    file : str
        Path to data file.
    """
    ierr = 0
    if not os.path.exists(file):
        print("Error file does not exist: {}".format(file))
        ierr = 1
    return ierr


def read_as_df(file):
    """
    Reads in the given file and returns it as a pandas dataframe.
    This function assumes that data in the file is seperated with whitespace.

    Parameters
    ----------
    file : str
        Path to data file.


    Returns
    --------
    df :  DataFrame, None if file does not exist.
    """

    ierr = check_exists(file)

    if ierr == 0:  # file exists
        df = pd.read_csv(file, sep="\s+")  # noqa
    else:  # file does not exit
        df = None
    return df


def drop_low_variance_df(df, var_threshold):
    """
    Drop columns from the data frame with variance below a threshold.

    Parameters
    ---------
    df : Dataframe
        Dataframe where colummns need to be dropped.

    Returns
    -------
    df_out :  Dataframe
        Datafame with columns dropped.
    """

    # Get the columns to drop
    columns_to_drop = [col for col in df.columns if df.var()[col] < var_threshold]

    # Print a message about the columns to drop
    print(
        """These columns will be discarded as their
        variance is below the set threshold""",
        columns_to_drop,
    )

    # Drop the columns from the data frame
    df_out = df.drop(columns=columns_to_drop)

    return df_out


def read_as_array(file, names=None, skip_header=0):
    """
    Reads in the given file and returns in as a numpy array.

    Parameters
    ----------
    file : str
        File to be read in.

    names : {None, True, str, sequence}, optional
        If `names` is True, the field names are read from the first line after
        the first `skip_header` lines. This line can optionally be preceded
        by a comment delimiter. If `names` is a sequence or a single-string of
        comma-separated names, the names will be used to define the field names
        in a structured dtype. If `names` is None, the names of the dtype
        fields will be used, if any.

    skip_header : int, optional
        The number of lines to skip at the beginning of the file.

    Returns
    --------
    array : ndarray, None if file does not exist.
    """

    ierr = check_exists(file)
    if ierr == 0:  # file exists
        array = np.genfromtxt(file, names=names, skip_header=skip_header)
    else:  # file does not exist
        array = None
    return array


def clean_nans(array):
    """
    Replaces nans in the array with zeros.

    Parameters
    ----------
    array : ndarray
        Array with nans to be cleaned.

    Returns
    -------
    clean_array : ndarray
        Array with nans replaced by zero.
    """

    clean_array = np.nan_to_num(array)
    return clean_array


# Functions which deal with text output of data


def save_df(df, output_file, header=True, index=False):
    """
    Saves the data frame to the output file.

    Arguments
    ---------
    df : Dataframe
        Dataframe to be saved.

    output_file : str
        Path where the Dataframe will be saved.

    header : bool or list of str, default True
            Write out the column names. If a list of strings is given it is
            assumed to be aliases for the column names.

    index : bool, default False
            Write row names (index).
    """

    df.to_csv(output_file, sep="\t", header=header, index=index)


def save_array(array, output_file, header=""):
    """
    Saves the array to the output file.

    Arguments
    ---------
    array : ndarray
        Array to be saved.

    output_file : str
        Path to where the array will be saved.

    header : str, optional
        String that will be written at the beginning of the file.
    """

    np.savetxt(output_file, array, header=header)
