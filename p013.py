sum = 0

file = open('p013.txt', 'r')
for line in file.readlines():
    sum += int(line)
print(sum)