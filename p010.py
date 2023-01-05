import p007

i = 0
sum = 0
for i in range(0, 2000000):
    if p007.is_prime(i):
        sum += i
print(sum)