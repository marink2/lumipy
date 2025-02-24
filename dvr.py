import numpy as np
import scipy as sp

def dvr(r, e, mu):
    """
    Discrete Value Representation (DVR) 1-Dimensional

        r  : (array) potential surface position values
        e  : (array) potential surface energy values
        mu : (float) reduce mass
    """

    N = len(r)
    mp = (r[-1] - r[0]) / N
    curve = sp.interp1d(r, e)

    H = np.ndarray((N,N), dtype="float")

    for i in range(N):
        for j in range(N):
            if(i == j):
                H[i][j] = (1 / (2 * mu * mp**2)) * (np.pi**2 / 3) + curve(i * mp)

            else:
                H[i][j] = (-1)**(i - j) * (1 / (2 * mu * mp**2)) * (2/ (i-j)**2)

    Ev, eigvec = np.linalg.eigh(H)
    Cv = eigvec.transpose()
    
    return [Ev, Cv]