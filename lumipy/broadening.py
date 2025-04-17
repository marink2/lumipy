import numpy as np

def lorentz(e, f, y=0.2, scale=1, bounds=None, offset=None, npts=10000):
    """
    Lorentzian convolution function
        e       : energy values, can be given as a number or array of numbers
        f       : intensity values, can be given as a number or array of numbers
        y       : gamma broadening factor (FWHM)
        scale   : scaling factor
        bounds  : (min, max) range for energy axis
        offset  : extension beyond bounds
        npts    : number of points on energy axis
    """

    e = np.asarray(e)
    f = np.asarray(f)

    if e.shape != f.shape:
        raise ValueError(f'e and f must have same dimension, but have shapes {e.shape} and {f.shape}')

    # make spectrum range
    s = offset or (4 * y)
    b = bounds or (e.min(), e.max())
    x = np.linspace(b[0] - s, b[1] + s, npts)

    # compute lorentzian spectrum
    spectrum = scale * f[..., np.newaxis] * (0.5 * y / np.pi) / (0.25 * y**2 + (x - e[..., np.newaxis])**2)

    return x, spectrum.squeeze()

def gaussian(e, f, y=0.2, scale=1, bounds=None, offset=None, npts=10000):
    # TODO: implement gaussian convolution function
    pass