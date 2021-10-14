input = []

with open('input.txt') as fin:
    for line in fin:
        input.append([str(x) for x in line.split()])

a = input.pop(0)
b = input.pop(0)
X = int(b[0])
side = a[0]

with open('output.txt','w') as fout:
    if side == "Home":
        fout.write("Yes")
    elif X%2 == 0:
        fout.write("No")
    else:
        fout.write("Yes")
