# %% External package import
from numpy import sqrt
from numpy import sum as nsum

# %% Statistical analysis functions


def correlate(data, method="pearson", drop_cols=None, return_sorted=True):
    """
    Calculate the correlation of the data columns.

    Parameters
    ----------
    data : Dataframe
        Pandas dataframe with the columns for which to calculate the \
        correlation.

    method : string, default='pearson'
        Correlation method as a string.

    drop_cols : iterable, default=None
        Iterable with data columns to drop before correlating.

    return_sorted : bool, default=True
        Indicator for sorting the output by absolute correlation value.

    Returns
    -------
    Dataframe
        Pandas dataframe with the (sorted) correlation values between the \
        data columns.
    """

    # Check if colums should be dropped
    if drop_cols:
        # Drop the columns from the data
        data.drop(columns=drop_cols)

    # Calculate the correlation matrix
    corr_matrix = data.corr(method=method)

    # Set the diagonal elements of the correlation matrix to None
    for i in range(corr_matrix.shape[0]):
        corr_matrix.iloc[i, i] = None

    # Stack the correlation matrix into a table and reset the index
    corr_table = corr_matrix.stack().reset_index()

    # Set the column names for the table
    corr_table.columns = ["var0", "var1", "corr"]

    # Check if the values should be sorted
    if return_sorted:
        # Sort the table by the absolute correlation values and reset the index
        corr_table = corr_table.sort_values(
            by="corr", ascending=False, key=abs
        ).reset_index(drop=True)

    return corr_table


def compute_euclidean_distance(x, y):
    """
    Compute the euclidean distance between two vectors.

    Parameters
    ----------
    x : array
        Array with the values of the first vector.

    y : array
        Array with the values of the second vector.

    Returns
    -------
    float
        Euclidean distance between x and y.
    """

    return sqrt(nsum(x - y) ** 2)
