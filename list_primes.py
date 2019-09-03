import time
start = time.time()

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        end = time.time()
        if end - start > 3000:
            break
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

print(get_primes(100000))