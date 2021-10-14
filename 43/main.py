input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([str(x) for x in line.split()])

list = input.pop(0)
a = str(list[0])

c = 0
max = 0
for i in a:
    if i == "0":
        c = c + 1
        if c > max:
            max = c
    else:
        c = 0

with open('output.txt','w') as fout:
    fout.write(str(max))
