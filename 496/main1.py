input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

tmp = input.pop(0)
n = tmp[0]
list = input.pop(0)
list.append(list[0])
list.append(list[1])
print(list)
s = 0
counter = 0
for i in range(n-1):
    print("i = ", i)
    counter = list[i] + list[i+1] + list[i+2]
    print("counter = ", counter)
    if counter > s:
        s = counter
        print("s = ", s)

with open('output.txt','w') as fout:
    fout.write(str(s))
