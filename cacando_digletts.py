N = input()
s = input()

def gcd(a, b):
    mod = a % b

    while mod > 0:
        a = mod
        mod = b % mod
        b = a
        
    return b

def mmc(a, b):
    return (a * b) / gcd(a, b)

A = s.split(' ')
B = A.copy()
nums = []

ini_cycle = 1
k = 0
r = len(A) + 1
count = 1

while r > 0:
    index = int(B[k]) -1
    A[k] = -1
    count += 1

    k = index

    if int(B[index]) == int(ini_cycle):
        A[index] = -1
        for i in range(len(A)):
            if int(A[i]) >= 0:
                ini_cycle = A[i]
                
                k = i
                break   
        nums.append(count)  
        count = 0
    r -= 1

x = nums[0]
for i in range(len(nums) -1):
	x = mmc(x, nums[i+1])

print(int(x)) 
	
