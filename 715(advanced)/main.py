input = []

with open("input.txt") as fin:
    line = fin.readline().split(' ')
    n, m = int(line[0]), int(line[1])
    for line in fin:
        input.append([list(x) for x in line.split()])

new_list1 = []
new_list2 = []

for i in range(n):
    new_list1.append(input[i][0])

for i in range(n+1,(n*2)+1):
    new_list2.append(input[i][0])

counter = 0

for i in range(n):
    for j in range(m):
        if new_list1[i][j] == new_list2[i][j]:
            counter += 1

print(counter)
