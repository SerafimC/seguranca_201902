def expo(n, e, m):
    if (e == 0):
        return 1
    if (e % 2 == 1):
        return (expo(n, e-1, m) * n) % m
    aux = expo(n, e/2, m)
    return (aux**2) % m

for a in range(5):
    for e in [3, 5, 7]:
        print("%i^%i mod(%i): %i"%(a+1, e-1, e, expo(a+1, e-1, e)))
