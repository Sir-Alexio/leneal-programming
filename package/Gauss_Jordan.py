
def gauss_jordan(maxColomn, minString, matrix, rightSide):
    coef = matrix[minString][maxColomn]

    for i in range(len(matrix[0])):  # делим ведущую строку на коэффициент
        matrix[minString][i] /= coef

    rightSide[minString] /= coef  # делим правый столбец на коэффициент

    for i in range(len(matrix)):  # получаем новые строки

        if i == minString:
            continue

        coef = matrix[i][maxColomn]  # находим новый коэффициент

        for j in range(len(matrix[0])):  # идем по столбцам и получаем новые элементы строк
            matrix[i][j] -= matrix[minString][j] * coef

        rightSide[i] -= rightSide[minString] * coef  # получаем новые элементы правого столбца
