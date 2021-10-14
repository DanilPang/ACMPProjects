input = []

with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

list = input.pop(0)
N = list[0]
A = list[1]
B = list[2]

SN = N * A * B * 2

with open('output.txt','w') as fout:
    fout.write(str(SN))
