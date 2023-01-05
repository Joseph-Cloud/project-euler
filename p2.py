total = 0
i0 = 1
i1 = 2

while True:
    if i1 > 4000000:
        break
    if i1 % 2 == 0:
        total += i1
    t = i0
    i0 = i1
    i1 = i0 + t

print(total)