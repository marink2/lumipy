def moorse(r, D=1, a=1, re=1, y=0):
    y = D * (1-np.exp(-a * (r-re) ))**2 + y
    return y