"""
Wrapper function for making color maps from lists
of colors.
"""

from matplotlib.colors import LinearSegmentedColormap
from typing import Tuple, List


def make_custom_cmap(name: str, colors: List) -> Tuple[LinearSegmentedColormap]:
    """
    Makes a custom color map from your set of colors, and returns
    it along with a 'reversed' version.

    Parameters
    ----------

    name: str
        Base name for your color map.

    colors: List[List[int]]
        List of colors (from bottom to top) as 8-bit integers. Max is
        255, so:

        .. code-block:: python

            colors = [
                [0, 0, 0],
                [255, 255, 255]
            ]

        would produce a color map from black to white.


    Returns
    -------

    cmap: LinearSegmentedColormap
        Base colour map, made from your colors.

    cmap_r: LinearSegmentedColormap
        Reversed version of your color map.
    """

    float_colors = [[x / 255 for x in color] for color in colors]

    cmap = LinearSegmentedColormap.from_list(name, float_colors, N=1024)

    cmap_r = LinearSegmentedColormap.from_list(
        f"{name}_r", list(reversed(float_colors)), N=1024
    )

    return cmap, cmap_r
