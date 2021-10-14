input = []
with open('input.txt') as fin:
    for line in fin:
        input.append([str(x) for x in line.split()])

tmp = input.pop(0)
a = tmp[0]
if (a[0] == a[3] and a[1] == a[2]):
    with open('output.txt','w') as fout:
        fout.write("YES")
else:
    with open('output.txt','w') as fout:
        fout.write("NO")
