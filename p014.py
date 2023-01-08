def sequence(n):
    total = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        total += 1
    return total

max = 0
max_i = 0
for i in range(2, 1000000):
    seq = sequence(i)
    if seq > max:
        max = seq
        max_i = i
print(max_i)