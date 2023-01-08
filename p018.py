# read in first number as prev[0]
# for each elem in each line
#   compare possible parents to find best sum
# traverse list of best path sums and return highest

# prev[0]
# curr[0] -> prev[0]
# curr[1] -> prev[0]
# prev = cur
# cur[0] -> prev[0]
# cur[1] -> prev[0] vs prev[1]
# cur[2] -> prev[1]

file = open('p018.txt', 'r')
prev = [int(file.readline())]
for line in file.readlines():
    line = line.split()
    curr = [int(line[0]) + prev[0]]
    for i in range(1, len(line) - 1):
        curr.append(int(line[i]) + max(prev[i - 1], prev[i]))
    curr.append(prev[len(prev) - 1] + int(line[len(line) - 1]))
    prev = curr
print(max(prev))