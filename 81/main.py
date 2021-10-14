input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

input.pop(0)
list = input.pop(0)

min = list[0]
max = 0
c = 0
for i in list:
    c = i
    if c > max:
        max = c
    if c < min:
        min = c

mylist = [min, max]
print(mylist)
with open('output.txt','w') as fout:
    for i in mylist:
        fout.write(str(i))
        fout.write(" ")
