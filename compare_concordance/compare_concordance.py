"""Statistical inference about correlated right-censored C-indices."""

import ctypes

import numpy as np

import scipy as sp
import scipy.stats

from .bindings import compareC


def compare_concordance(time, status, score_y, score_z):
    concordance_y = estimate_concordance(time, status, score_y)
    concordance_z = estimate_concordance(time, status, score_z)

    diff = concordance_y - concordance_z

    vardiff, var_y, var_z, cov = _compute_vardiff(time, status, score_y, score_z)

    zscore = diff / np.sqrt(vardiff)

    pval = 2 * (1.0 - sp.stats.norm.cdf(np.abs(zscore)))

    return concordance_y, concordance_z, diff, zscore, pval


def estimate_concordance(time, status, score):
    timeX = np.asarray(time).astype(np.float64)
    timeX = timeX.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    statusX = np.asarray(status).astype(np.int32)
    statusX = statusX.ctypes.data_as(ctypes.POINTER(ctypes.c_int))

    scoreY = np.asarray(score).astype(np.float64)
    scoreY = scoreY.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    nobs = ctypes.c_int(len(time))

    t11 = compareC.TauXX(timeX, statusX, nobs)
    t12 = compareC.TauXY(timeX, statusX, scoreY, nobs)

    concordance = (1.0 + t12 / t11) / 2.0

    return concordance


def _compute_vardiff(time, status, score_y, score_z):
    timeX = np.asarray(time).astype(np.float64)
    timeX = timeX.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    statusX = np.asarray(status).astype(np.int32)
    statusX = statusX.ctypes.data_as(ctypes.POINTER(ctypes.c_int))

    scoreY = np.asarray(score_y).astype(np.float64)
    scoreY = scoreY.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    scoreZ = np.asarray(score_z).astype(np.float64)
    scoreZ = scoreZ.ctypes.data_as(ctypes.POINTER(ctypes.c_double))

    nobs = ctypes.c_int(len(time))

    t11 = compareC.TauXX(timeX, statusX, nobs)
    t12 = compareC.TauXY(timeX, statusX, scoreY, nobs)
    t13 = compareC.TauXY(timeX, statusX, scoreZ, nobs)
    var_t11 = compareC.VarTauXX(timeX, statusX, nobs)
    var_t12 = compareC.VarTauXY(timeX, statusX, scoreY, nobs)
    var_t13 = compareC.VarTauXY(timeX, statusX, scoreZ, nobs)
    cov_t1112 = compareC.CovTauXXXY(timeX, statusX, scoreY, nobs)
    cov_t1113 = compareC.CovTauXXXY(timeX, statusX, scoreZ, nobs)
    cov_t1213 = compareC.CovTauXYXZ(timeX, statusX, scoreY, scoreZ, nobs)

    _v2 = np.asarray([1 / t11, -t12 / t11**2])
    _m = np.asarray([[var_t12, cov_t1112], [cov_t1112, var_t11]])
    est_varCxy = np.matmul(_v2, np.matmul(_m, _v2)) / 4.0

    _v3 = np.asarray([1 / t11, -t13 / t11**2])
    _m = np.asarray([[var_t13, cov_t1113], [cov_t1113, var_t11]])
    est_varCxz = np.matmul(_v3, np.matmul(_m, _v3)) / 4.0

    _m = np.asarray([[cov_t1213, cov_t1112], [cov_t1113, var_t11]])
    est_cov = np.matmul(_v2, np.matmul(_m, _v3)) / 4.0

    est_vardiff_c = est_varCxy + est_varCxz - 2 * est_cov

    return est_vardiff_c, est_varCxy, est_varCxz, est_cov
