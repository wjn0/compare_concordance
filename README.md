compare\_concordance
====================

This Python package implements a statistical test for the comparison of correlated right-censored concordance indices. The code is derived entirely from the GPLv3-licensed R package [compareC](https://cran.r-project.org/web/packages/compareC/index.html). Accordingly, this package is also licensed under GPLv3. If you use it in published work, you should cite the original authors' paper (see below).

Installation
------------

This package can be installed via Pip:

    $ pip install compare_concordance

Usage
-----

```python
from compare_concordance import compare_concordance

scores_1 = model1.predict(x)
scores_2 = model2.predict(x)

concordance_1, concordance_2, difference, zscore, pvalue = compare_concordance(
    y['time'],
    y['status'],
    scores_1,
    scores_2
)
```

Motivation
----------

When one has two risk scores they wish to evaluate with respect to a right-censored survival outcome, the two scores are likely to be correlated. That is, a patient deemed higher-risk by one score is likely also deemed higher-risk by the other score. Therefore, when assessing the statistical significance of the difference in c-index of the two risk scores, the variance estimate will be closer to the true variance (lower) if you account for this correlation (conferring higher power). Kang et al. (2015) provides a closed-form for the variance. This is a simple port of the authors' R package to Python, with NumPy-compatible bindings for their existing C code and a Python implementation of the baseline they compare to (bootstrapping).

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

Please also consider citing this repository if you use this implementation.
