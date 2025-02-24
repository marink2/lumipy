def lorentz(e, f, eRange, y=0.2):
    """
    Lorentzian Convolution

        e       : (array) transition energy values
        f       : (array) oscillator strength values
        eRange  : (array) energy range for spectrum plot
        y       : (float) Lorentz curve broadening factor 
    """

    lorentz_conv = np.zeros_like(eRange)

    for i in range(len(e)):
        l_curve =  f[i] * (y / (2 * np.pi)) / ((y/2)**2 + (eRange - e[i])**2)
        lorentz_conv = lorentz_conv + l_curve

    return lorentz_conv