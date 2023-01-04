import unittest

import numpy as np

from compare_concordance import compare_concordance


class TestCompareConcordance(unittest.TestCase):
    def test_compare_concordance(self):
        n = 1000
        time = np.random.choice(1000, size=n)
        status = np.random.choice(2, size=n)
        score_1 = np.random.randn(n)
        score_2 = np.random.randn(n)

        compare_concordance(time, status, score_1, score_2)
