
def product(fracs):
    #t = reduce(fra)
    t=reduce(lambda frac1,frac2:frac1*frac2, fracs)
    return t.numerator, t.denominator