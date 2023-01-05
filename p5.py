def divisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

i = 0

while True:
    i += 1
    if divisible(i):
        print(i)
        exit()