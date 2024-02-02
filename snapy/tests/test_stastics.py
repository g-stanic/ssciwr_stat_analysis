import numpy as np
import pandas as pd
import get_statistics


def test_correlate():
    """Test the calculation of pearson correlation
    coefficents using known correlations."""

    rng = np.random.default_rng(12345)

    test_size = 100000
    test_array = np.zeros([test_size, 5])
    test_array[:, 0] = np.arange(test_size)
    test_array[:, 1] = np.arange(test_size) * 2 + 1  # Full positive correlation
    test_array[:, 2] = np.arange(test_size) * -2 + 1  # Full negative correlation
    test_array[:, 3] = rng.random(test_size)  # Random
    test_array[:, 4] = np.arange(test_size) ** 2  # Partial Correlation
    test_df = pd.DataFrame(test_array, columns=["var1", "var2", "var3", "var4", "var5"])

    expected = pd.DataFrame(
        [
            ["var1", "var2", 1.0],
            ["var1", "var3", -1.0],
            ["var1", "var5", 0.9682452314018],
            ["var3", "var5", -0.9682452314018],
            ["var1", "var4", 0.0024152004945614813],
            ["var3", "var4", -0.0024152004945614813],
            ["var4", "var5", 0.0009700467915621443],
        ],
        columns=["var0", "var1", "corr"],
    )

    assert expected.equals(
        get_statistics.correlate(test_df, method="pearson", return_sorted=True)
    )


def test_compute_euclidean_distance():
    """Test the euclidiean distances of reference vectors."""

    x1 = np.ones(2)
    y1 = np.ones(2) * 2
    assert get_statistics.compute_euclidean_distance(x1, y1) == 2
    assert get_statistics.compute_euclidean_distance(x1, x1) == 0


test_compute_euclidean_distance()
test_correlate()
