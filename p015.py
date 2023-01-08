import math

def path(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return path(x - 1, y) + path(x, y - 1)

print(math.factorial(20)/(math.factorial(10) * math.factorial(10)))
print(path(10, 10))