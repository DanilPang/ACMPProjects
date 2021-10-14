
input = []

with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

mylist = input.pop(0)

square = mylist[0] * mylist[0]

output = str(square)
with open('output.txt','w') as fout:
    fout.write(output)
