Taylor Swift color map collection.

Includes color maps based on the following albums:

+ Red (red, red_r)
+ 1989 (nineteen_eighty_nine, nineteen_eighty_nine_r)
+ Reputation (reputation, reputation_r)
+ Lover (lover, lover_r)
+ Folklore (folklore, folklore_r)
+ Evermore (evermore, evermore_r, evermore_shifted, evermore_shifted_r)

License: LGPLv3
Author: Josh Borrow (josh@joshborrow.com)

Usage
-----

To use these, you can import them and use them
with matplotlib as you would with any other color map.

```python
from swiftascmaps import red
from matplotlib.pyplot import imshow
from numpy import random

imshow(random.rand(128, 128), cmap=red)
```

Examples
--------

### Red

![](images/red.png)

### 1989

![](images/1989.png)

### Reputation

![](images/reputation.png)

### Lover

![](images/lover.png)

### Folklore

![](images/folklore.png)

### Evermore

![](images/evermore.png)

### Evermore shifted

![](images/evermore_shifted.png)


Note
----

Of course, these aren't necessarily designed to be colorblind
friendly, or perceptually uniform, so use them with caution.
They are quite pretty though. To underline how much you should
_not_ use these in a real scientific publication (apart from
perhaps qualitative imaging), the lightness values are shown
below.

![](images/lightness.png)

For quantitative comparisons, please ensure that you use a
perceptually uniform colour map (see e.g. those available
directly through [matplotlib](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)).
