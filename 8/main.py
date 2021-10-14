input = []

with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

mylist = input.pop(0)

div = mylist[0] * mylist[1]

with open('output.txt','w') as fout:
    if div == mylist[2]:
        fout.write("YES")
    else:
        fout.write("NO")
