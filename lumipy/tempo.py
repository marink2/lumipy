import numpy as np
from broadening import lorentz

def tempo(t, e, f, y=0.2, scale=1, bounds=None, offset=None, npts=10000):
    """
    Tempo is a 2D convolution function (energy and time)
        t       : time values, can be given as a number or array of numbers
        e       : energy values, can be given as a number or array of numbers
        f       : intensity values, can be given as a number or array of numbers
        y       : gamma broadening factor (FWHM)
        scale   : scaling factor
        bounds  : (min, max) range for energy axis
        offset  : extension beyond bounds
        npts    : number of points on energy axis
    """

    x, spectrum = lorentz(e, f, y=y, scale=scale, bounds=bounds, offset=offset, npts=npts)
    spectrum2D = 0

    return x, t, spectrum2D