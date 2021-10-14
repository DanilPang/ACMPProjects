input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

tmp = input.pop(0)
n = tmp[0]
list = input.pop(0)
list.append(list[0])
list.append(list[1])
s = 0
if list[1] > list[n-2]:
    s = list[0] + list[n-1] + list[1]
else:
    s = list[0] + list[n-1] + list[n-2]

for i in range(1,n-1):
    if (list[i-1] + list[i] + list[i+1]) > s:
        s = list[i-1] + list[i] + list[i+1]
        print(s)

with open('output.txt','w') as fout:
    fout.write(str(s))
