def proj_a(n, r):
    return n + r

mult_3 = 0
mult_5 = 0

while mult_3 < 1000000:
    mult_3 += proj_a(mult_3, 3) if proj_a(mult_3, 3) % 5 != 0 else 0

while mult_5 < 1000000:
    mult_5 += proj_a(mult_5, 5) 

print(mult_3 + mult_5)