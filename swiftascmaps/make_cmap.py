"""
Wrapper function for making color maps from lists
of colors.
"""

from matplotlib.cm import register_cmap
from matplotlib.colors import LinearSegmentedColormap
from typing import List, Tuple


def hex_to_rgb(colors: List[str]) -> List[List[int]]:
    """
    Converts colors from hex codes to 8-bit integer RGB values.

    Parameters
    ----------

    colors: List[str]
        Your hex codes, e.g. ["#000000"]

    Returns
    -------

    rgb_colors: List[List[int]]
        List of colors formatted as rgb [[0, 0, 0]]
    """

    rgb_colors = []

    for color in colors:
        rgb_colors.append(
            list(int(color[1:][i:i+2], 16) for i in (0, 2, 4))
        )

    return rgb_colors


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

    cmap = LinearSegmentedColormap.from_list(f"swift.{name}", float_colors, N=1024)

    cmap_r = LinearSegmentedColormap.from_list(
        f"swift.{name}_r", list(reversed(float_colors)), N=1024
    )

    register_cmap(cmap=cmap)
    register_cmap(cmap=cmap_r)
    
    return cmap, cmap_r
