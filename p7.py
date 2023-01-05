import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

i = 0
ith = 0
while True:
    i += 1
    if is_prime(i):
        ith += 1
        if ith >= 10001:
            print(i)
            break