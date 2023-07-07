## Taylor Swift color map collection.

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5649259.svg)](https://doi.org/10.5281/zenodo.5649259)

Quick start: `pip install swiftascmaps`

Includes color maps based on the following albums:

+ Red (`red`, `red_r`)
+ 1989 (`nineteen_eighty_nine`, `nineteen_eighty_nine_r`)
+ Reputation (`reputation`, `reputation_r`)
+ Lover (`lover`, `lover_r`)
+ Folklore (`folklore`, `folklore_r`)
+ Evermore (`evermore`, `evermore_r`, `evermore_shifted`, `evermore_shifted_r`)
+ Fearless: Taylor's Version (`fearless_tv`, `fearless_tv_r`)
+ Red: Taylor's Version (`red_tv`, `red_tv_r`)
+ Midnights (`midnights`, `midnights_r`)
+ Speak Now: Taylor's Version (`speak_now_tv`, `speak_now_tv_r`)

License: LGPLv3
Author: Josh Borrow (josh@joshborrow.com)

If you prefer to use `R`, there is an alternative package
maintained as [taloRswift](https://github.com/asteves/tayloRswift).

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

The color maps can also be accessed in matplotlib using strings
by prefixing `swift`, e.g.

```python
import swiftascmaps

imshow(random.rand(128, 128), cmap="swift.red")
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

### Fearless: Taylor's Version

![](images/fearless_tv.png)

### Red: Taylor's Version

![](images/red_tv.jpg)

### Midnights

![](images/midnights.png)

### Speak Now (Taylor's Version)

![](images/speak_now_tv.jpg)

Note
----

Of course, these aren't necessarily designed to be colorblind
friendly, or perceptually uniform, so use them with caution.
They are quite pretty though. To underline how much you should
_not_ use these in a real scientific publication (apart from
perhaps qualitative imaging), the lightness values are shown
below.

![](images/lightness_swift_as_cmaps.png)
![](images/lightness_cmaps_re_recordings.png)
![](images/midnights_uniformity.png)
![](images/speak_now_tv_uniformity.png)

For quantitative comparisons, please ensure that you use a
perceptually uniform colour map (see e.g. those available
directly through [matplotlib](https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html)).
