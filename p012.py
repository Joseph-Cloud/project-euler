import math

def triangle(n):
    sum = n
    for i in range(n):
        sum += i
    return sum

def num_factors(n):
    if n == 1:
        return 1
    
    sum = 2
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        sum += 1
    sqrt = math.ceil(sqrt)
    for i in range(2, sqrt):
        if n % i == 0:
            sum += 2
    return sum

i = 1
tri = 1
while True:
    i += 1
    tri += i
    num = num_factors(tri)
    if num > 500:
        print(tri)
        break