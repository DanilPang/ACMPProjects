def coord_finder(i, j, z):
    x, y = 0, 0

    if z == 0:
        x = i - 1
        y = j - 1

    if z == 1:
        x = i - 1
        y = j

    if z == 2:
        x = i - 1
        y = j + 1

    if z == 3:
        x = i
        y = j - 1

    if z == 4:
        x = i
        y = j + 1

    if z == 5:
        x = i + 1
        y = j - 1

    if z == 6:
        x = i + 1
        y = j

    if z == 7:
        x = i + 1
        y = j + 1

    if x == -1:
        x = n - 1

    if y == -1:
        y = m - 1

    if x == n:
        x = 0

    if y == m:
        y = 0

    return x, y


input = []

with open("input.txt") as fin:
    line = fin.readline().split(' ')
    n, m, k = int(line[0]), int(line[1]), int(line[2])
    for i in fin:
        input.append([list(x) for x in i.split()])

Generation = []
New_Generation = [[0 for j in range(m)] for i in range(n)]

for i in range(len(input)):
    Generation.append(input[i][0])

while k > 0:
    k -= 1
    for i in range(n):
        for j in range(m):

            counter = 0

            for z in range(8):

                XY = coord_finder(i, j, z)

                if Generation[XY[0]][XY[1]] == "*":
                    counter += 1


            if Generation[i][j] == ".":
                if counter == 3:
                    New_Generation[i][j] = "*"
                else:
                    New_Generation[i][j] = "."

            if Generation[i][j] == "*":
                if counter > 3 or counter < 2:
                    New_Generation[i][j] = "."
                else:
                    New_Generation[i][j] = "*"
    for i in range(n):
        for j in range(m):
            Generation[i][j] = New_Generation[i][j]

with open("output.txt", "w") as fout:
    for i in range(n):
        for j in range(m):
            fout.write(Generation[i][j])
        fout.write("\n")