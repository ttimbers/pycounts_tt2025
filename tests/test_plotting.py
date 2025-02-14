import pycounts_tt2025
import pytest
import matplotlib.pyplot as plt


@pytest.mark.mpl_image_compare
def test_plot_words():
    counts = pycounts_tt2025.count_words("tests/einstein.txt")
    fig = pycounts_tt2025.plot_words(counts, n=10)
    return fig