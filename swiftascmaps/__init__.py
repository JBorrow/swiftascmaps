"""
Taylor Swift color map collection.

Includes color maps based on the following albums:

+ Red (red, red_r)
+ 1989 (nineteen_eighty_nine, nineteen_eighty_nine_r)
+ Reputation (reputation, reputation_r)
+ Lover (lover, lover_r)
+ Folklore (folklore, folklore_r)

License: LGPLv3
Author: Josh Borrow (josh.borrow@gmail.com)

Usage
-----

To use these, you can import them and use them
with matplotlib as you would with any other color map.

.. code-block:: python

    from swiftascmaps import red
    from matplotlib.pyplot import imshow
    from numpy import random

    imshow(random.rand(128, 128), cmap=red)

"""

import swiftascmaps.colors as colors
from swiftascmaps.make_cmap import make_custom_cmap
from swiftascmaps.__version__ import __version__

red, red_r = make_custom_cmap("red", colors.red)
nineteen_eighty_nine, nineteen_eighty_nine_r = make_custom_cmap(
    "nineteen_eighty_nine", colors.nineteen_eighty_nine
)
reputation, reputation_r = make_custom_cmap("reputation", colors.reputation)
lover, lover_r = make_custom_cmap("lover", colors.lover)
folklore, folklore_r = make_custom_cmap("folklore", colors.folklore)
