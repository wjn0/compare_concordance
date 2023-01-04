import os

import ctypes
from ctypes import cdll, util

import pathlib

import numpy as np


libfile = pathlib.Path(__file__).parent / "compareC.so"
compareC = cdll.LoadLibrary(str(libfile))


compareC.TauXX.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
compareC.TauXX.restype = ctypes.c_double

compareC.TauXY.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
]
compareC.TauXY.restype = ctypes.c_double

compareC.VarTauXX.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int,
]
compareC.VarTauXX.restype = ctypes.c_double

compareC.VarTauXY.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
]
compareC.VarTauXY.restype = ctypes.c_double

compareC.CovTauXXXY.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
]
compareC.CovTauXXXY.restype = ctypes.c_double

compareC.CovTauXYXZ.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int,
]
compareC.CovTauXYXZ.restype = ctypes.c_double
