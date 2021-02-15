compare\_concordance
====================

This Python package implements a statistical test for the comparison of correlated right-censored concordance indices. The code is derived entirely from the GPLv3-licensed R package [compareC](https://cran.r-project.org/web/packages/compareC/index.html). Accordingly, this package is also licensed under GPLv3. If you use it in published work, you should cite the original authors' paper (see below).

Installation
------------

First, build the C library:

    $ python3 setup.py build_ext

Then, install using Pip:

    $ pip3 install .

This has been tested on 64-bit Linux with GCC version 7.5.0 and Python 3.6. If the installation step fails, it may be because your system names the .so file differently than expected.

Usage
-----

```python
from compare_concordance import compare_concordance

scores_1 = model1.predict(x)
scores_2 = model2.predict(x)

concordance_1, concordance2, difference, zscore, pvalue = compare_concordance(
    y['time'],
    y['status'],
    scores_1,
    scores_2
)
```

Citation
--------

> Kang L, Chen W, Petrick NA and Gallas BD (2015). "Comparing two correlated C indices with right-censored survival outcome: a one-shot nonparametric approach." Statistics in Medicine, 34(4), pp. 685-703. http://dx.doi.org/10.1002/sim.6370.

### Bibtex

    @Article{,
      title = {Comparing two correlated C indices with right-censored
        survival outcome: a one-shot nonparametric approach},
      author = {Le Kang and Weijie Chen and Nicholas A. Petrick and
        Brandon D. Gallas},
      year = {2015},
      volume = {34},
      number = {4},
      pages = {685-703},
      journal = {Statistics in Medicine},
      url = {http://dx.doi.org/10.1002/sim.6370},
    }

