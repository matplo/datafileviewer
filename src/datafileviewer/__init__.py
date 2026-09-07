"""datafileviewer — inspect ROOT, Parquet, HDF5, numpy, and pandas-readable
files from the terminal."""

from datafileviewer.core import Node, file_summary, tree_branch_info, walk_directory

__version__ = "1.0.2"

__all__ = ["Node", "file_summary", "tree_branch_info", "walk_directory", "__version__"]
