
def gcd(a, b):
    mod = a % b

    while mod > 0:
        a = mod
        mod = b % mod
        b = a
        
    return b

def invmul(n, mod):
    x = mod*(-1)
    md = x % mod

    while md != 1 and x < 0:
        x += 1
        md = n*x % mod

    return x % mod  if md == 1 else 0

print('Exercicio 1')
for i in range(21):
    print("Inverso multiplicativo %i mod(21): %i"%(i+1, invmul(i+1, 21)))

print('')
print('Exercicio 2')
print("Inverso multiplicativo 45 mod(94): %i"%(invmul(45, 94)))