def lorentz(E_arr, E0_arr, osc_arr, gamma=0.2):

    # Lorentzian Convolution
    #
    #   E_arr   : delta energy axis on which to calculate osc values according to L.C.
    #   E0_arr  : delta energy values where osc peaks exist
    #   osc_arr : value of osc at corresponding E0_arr index
    #   gamma   : Lorentz factor for time broadening
    #

    lorentz_conv = np.zeros(len(E_arr))

    for i in range(len(E0_arr)):
        l_curve =  osc_arr[i] * (gamma / (2 * np.pi)) / ((gamma/2)**2 + (E_arr - E0_arr[i])**2)
        lorentz_conv = lorentz_conv + l_curve

    return lorentz_conv