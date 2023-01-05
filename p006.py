def sum_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total

def square_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total ** 2

print(square_sum(100) - sum_squares(100))