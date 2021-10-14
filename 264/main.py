input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

N = input.pop(0)
mylist = input.pop(0)

counter = 0
max = 0
for i in mylist:
    if i > 0:
        counter += 1
    else:
        counter = 0
    if counter > max:
        max = counter

with open('output.txt','w') as fout:
    fout.write(str(max))
