import unittest

from compare_concordance import compare_concordance


class TestCompareConcordance(unittest.Testcase):
    def test_compare_concordance():
        n = 1000
        time = np.random.choice(1000, size=n)
        status = np.random.choice(2, size=n)
        score_1 = np.random.randn(n)
        score_2 = np.random.randn(n)

        compare_concordance(time, status, score_1, score_2)
