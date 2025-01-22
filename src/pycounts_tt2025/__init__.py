# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_tt2025")


from pycounts_tt2025.pycounts_tt2025 import count_words
from pycounts_tt2025.plotting import plot_words