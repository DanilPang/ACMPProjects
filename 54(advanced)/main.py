input = []

with open("input.txt") as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

NM = input.pop(0)
n = NM[0]
m = NM[1]

minarr = []
maxarr = []

for i in range(n):
    minarr.append(min(input[i]))
for i in range(m):
    c = [r[i] for r in input]
    maxarr.append(max(c))

print(max(minarr), min(maxarr))
