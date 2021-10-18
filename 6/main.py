coord = input()

list = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5], ['F', 6], ['G', 7], ['H', 8]]

if len(coord) == 5:
    if coord[0] in "ABCDEFGH" and coord[1] in "12345678" and coord[2] == '-' and coord[3] in "ABCDEFGH" and coord[4] in "12345678":
        x1, x2, y1, y2 = 0, 0, int(coord[1]), int(coord[4])
        for i in range(8):

            if coord[0] == list[i][0]:
                x1 = list[i][1]
            if coord[3] == list[i][0]:
                x2 = list[i][1]

        if ((x1 - x2) ** 2 + (y1 - y2) ** 2) == 5:
            print('YES')
        else:
            print('NO')
    else:
        print('ERROR')
else:
    print('ERROR')