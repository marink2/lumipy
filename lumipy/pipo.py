import numpy as np

def kramers_heisenberg(e, e1, e2, f1, f2, k=0.0):
    """
    Kramers-Heisenberg formula for inelastic scattering
        e   : energy values, can be given as a number or array of numbers
        e1  : energy values of the first state
        e2  : energy values of the second state
        f1  : intensity values of the first state
        f2  : intensity values of the second state
        k   : momentum transfer (default is zero)
    """

    # Convert inputs to numpy arrays for element-wise operations
    e = np.asarray(e)
    e1 = np.asarray(e1)
    e2 = np.asarray(e2)
    f1 = np.asarray(f1)
    f2 = np.asarray(f2)

    # Check if all input arrays have the same shape
    if not (e.shape == e1.shape == e2.shape == f1.shape == f2.shape):
        raise ValueError(f'All input arrays must have the same shape, but got {e.shape}, {e1.shape}, {e2.shape}, {f1.shape}, {f2.shape}')

    # Calculate the Kramers-Heisenberg formula
    result = (f1 * f2) / ((e - e1 - k)**2 + (f1 + f2)**2)

    return result