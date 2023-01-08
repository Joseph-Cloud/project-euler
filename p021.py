import math

def sum_factors(n):
    if n == 1:
        return 1
    
    sum = 1
    sqrt = math.sqrt(n)
    if sqrt.is_integer():
        sum += sqrt
    sqrt = math.ceil(sqrt)
    for i in range(2, sqrt):
        if n % i == 0:
            sum += i
            sum += int(n / i)
    return sum

sum = 0
for i in range(10000):
    sum_f = sum_factors(i)
    if sum_f != i and sum_factors(sum_f) == i:
        sum += i
print(sum)