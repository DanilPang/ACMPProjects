input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([int(x) for x in line.split()])

tmp = input.pop(0)
n = tmp[0]
list = input.pop(0)

sin = list[n-1] + list[0] + list[1]
sout = list[0] + list[n-1] + list[n-2]
s = 0
counter = 0
for i in list:
    if i == 0:
        continue
    if i == n - 1:
        break
    counter = list[i-1] + list[i] + list[i+1]
    if counter > s:
        s = counter

if sin > s:
    s = sin
if sout > s:
    s = sout

with open('output.txt','w') as fout:
    fout.write(str(s))
