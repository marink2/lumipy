import numpy as np
from scipy import interpolate


def dvr(r, e, mu, interp=False):
    """
    Discrete Value Representation (DVR) 1-Dimensional

        r   : (array) potential surface position values
        e   : (array) potential surface energy values
        mu  : (float) reduce mass
    """

    if interp:
        cs = interpolate.CubicSpline(r, e)
        r_new = np.linspace(r[0], r[-1], 500)
        e_new = cs(r_new)

        r = r_new
        e = e_new

    N = len(r)
    mp = (r[1] - r[0])

    H = np.ndarray((N,N), dtype="float")

    for i in range(N):
        for j in range(N):
            if(i == j):
                H[i][j] = (1 / (2 * mu * mp**2)) * (np.pi**2 / 3) + e[i]

            else:
                H[i][j] = (-1)**(i - j) * (1 / (2 * mu * mp**2)) * (2/ (i-j)**2)

    Ev, eigvec = np.linalg.eigh(H)
    Cv = eigvec.transpose()
    
    return [r, e, Cv, Ev]