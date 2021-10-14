input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

N = input.pop(0)

mylist = []
for i in input:
    mylist.append(i.pop(0))

max0 = 0
max1 = 0
for i in mylist:
    if i == 0:
        max0 = max0 + 1
    if i == 1:
        max1 = max1 + 1

if max0 < max1:
    N = max0
else:
    N = max1

with open('output.txt','w') as fout:
    fout.write(str(N))
