input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([str(x) for x in line.split()])

tmp = input.pop(0)
mylist = []
for i in input:
    mylist.append(i.pop(0))

counter = 0
for i in mylist:
    if i[0] == i[3]:
        counter += 1


with open('output.txt','w') as fout:
    fout.write(str(counter))
