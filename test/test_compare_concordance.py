import unittest

import numpy as np

from compare_concordance import compare_concordance


class TestCompareConcordance(unittest.TestCase):
    """
    Test the closed-form concordance approach.
    """

    def test_compare_concordance(self):
        """
        Test that the function runs, implying that the extension built
        successfully.
        """
        n = 1000
        time = np.random.choice(1000, size=n)
        status = np.random.choice(2, size=n)
        score_1 = np.random.randn(n)
        score_2 = np.random.randn(n)

        compare_concordance(time, status, score_1, score_2)
    
    def test_consistency(self):
        """
        Test the consistency with the R package.

        Tested against R 3.4.4 and compareC 1.3.2.

          > library(compareC)
          > compareC(c(50, 30,20, 10, 10), c(1, 0, 1, 0, 1), c(0.2, 0.2, 0.1, 0.2, -0.3), c(0.3, 0., 0.1, -0.3, 0.5))
          $est.c
          Cxy       Cxz
          1.0000000 0.1666667

          $est.diff_c
          [1] 0.8333333

          $est.vardiff_c
          [1] 0.04115226

          $est.varCxy
          [1] 1.619075e-16

          $est.varCxz
          [1] 0.04115226

          $est.cov
          [1] -5.396917e-17

          $zscore
          [1] 4.107919

          $pval
          [1] 3.992397e-05
        """
        time = [50, 30, 20, 10, 10]
        status = [1, 0, 1, 0, 1]
        score_1 = [0.2, 0.2, 0.1, 0.2, -0.3]
        score_2 = [0.3, 0., 0.1, -0.3, 0.5]

        result = compare_concordance(time, status, score_1, score_2)
        assert np.allclose(result[0], 1., atol=1e-6)
        assert np.allclose(result[1], 1./6., atol=1e-6)
        assert np.allclose(result[2], 5./6., atol=1e-6)
        assert np.allclose(result[3], 4.107919, atol=1e-6)
        assert np.allclose(result[4], 3.992397e-5, atol=1e-6)
