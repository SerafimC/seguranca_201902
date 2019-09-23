def expo(n, exponent, m):
    if exponent == 0:
        return 1
    if exponent % 2 == 1:
        return (expo(n, exponent-1, m) * n) % m
    aux = expo(n, exponent/2, m)
    return (aux**2) % m

for a in range(5):
    for exponent in [3, 5, 7]:
        print("%i^%i mod(%i): %i"%(a+1, exponent-1, exponent, expo(a+1, exponent-1, exponent)))
