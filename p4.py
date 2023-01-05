def palindromic(n):
    str_n = str(n)
    rev = str_n[::-1]
    if rev == str_n:
        return True
    else:
        return False

max = 0

for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        if palindromic(i * j) and i * j > max:
            max = i * j

print(max)