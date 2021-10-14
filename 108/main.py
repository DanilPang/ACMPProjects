input = []

with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

list = input.pop(0)
a = str(list[0])

with open('output.txt','w') as fout:
    fout.write(a)
