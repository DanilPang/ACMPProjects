input = []

with open("input.txt") as fin:
    line = fin.readline().split(' ')
    n, m = int(line[0]), int(line[1])
    for line in fin:
        input.append([list(x) for x in line.split()])

new_list = []
counter = 0

for i in range(len(input)):
    new_list.append(input[i][0])

for i in range(n):
    for j in range(m):

        if new_list[i][j] == ".":

            if i != 0 and j != 0 and i != n - 1 and j != m - 1: #Проверяем в центре
                if new_list[i][j+1] == "." and new_list[i][j-1] == "." and new_list[i+1][j] == "." and new_list[i-1][j] == ".":
                    counter += 1

            if i == 0 and j == 0:   #Проверяем левый верхний угол
                if new_list[i+1][j] == "." and new_list[i][j+1] == ".":
                    counter += 1

            if i == n - 1 and j == 0:   #Проверяем левый нижний угол
                if new_list[i][j+1] == "." and new_list[i-1][j] == ".":
                    counter += 1

            if i == 0 and j == m - 1:   #Проверяем правый верхний угол
                if new_list[i+1][j] == "." and new_list[i][j-1] == ".":
                    counter += 1

            if i == n - 1 and j == m - 1:   #Проверяем правый нижний угол
                if new_list[i-1][j] == "." and new_list[i][j-1] == ".":
                    counter += 1


            if i == 0 and j != 0 and j != m - 1: #Проверяем верхнюю сторону без углов
                if new_list[i+1][j] == "." and new_list[i][j-1] == "." and new_list[i][j+1] == ".":
                    counter += 1

            if j == 0 and i != 0 and i != n - 1: #Проверяем левую сторону без углов
                if new_list[i+1][j] == "." and new_list[i-1][j] == "." and new_list[i][j+1] == ".":
                    counter += 1

            if i == n - 1 and j != 0 and j != m - 1: #Проверяем нижнюю сторону без углов
                if new_list[i-1][j] == "." and new_list[i][j-1] == "." and new_list[i][j+1] == ".":
                    counter += 1

            if i != n - 1 and i != 0 and j == m - 1: #Проверяем правую сторону без углов
                if new_list[i+1][j] == "." and new_list[i-1][j] == "." and new_list[i][j-1] == ".":
                    counter += 1
            


with open("output.txt", "w") as fout:
    fout.write(str(counter))
