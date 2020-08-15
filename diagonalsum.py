def sum_diagonals(matrix):
    print(matrix)
    if len(matrix) == 1 and len(matrix[0]) == 0:
        return 0
    else:
        rm = [ele for ele in reversed(matrix)]
        x = 0
        y = 0
        sum1 = 0
        sum2 = 0
        for i in range(len(matrix)):
            sum1 += matrix[x][x]
            x += 1
        for i in range(len(matrix)):
            sum2 += rm[y][y]
            y += 1
        return sum1+sum2
