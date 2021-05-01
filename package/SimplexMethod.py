import Gauss_Jordan


def simplex(matrix, rightSide):
    maxResult = 0  # находим начальное решение

    basis = [i for i in range(len(matrix) - 2, len(matrix[0]))]

    # ------------------------------------------------------------

    while True:  # gause - jordan start

        max = 0

        maxIndex = 0

        for i in range(len(matrix[0])):  # условие оптимальности
            if max < matrix[0][i] > 0:
                max = matrix[0][i]
                maxIndex = i

        if max == 0:  # условие выхода
            make_solution(matrix, maxResult, basis,rightSide)
            return

        # -----------------------------------------------------------
        minimum = rightSide[1]  # выбор исключаемого элемента

        minIndex = 0

        for i in range(1, len(rightSide)):
            if matrix[i][maxIndex] == 0:
                continue
            result = rightSide[i] / matrix[i][maxIndex]
            if minimum > result:
                minimum = result
                minIndex = i

        basis.remove(basis[minIndex - 1])
        basis.append(maxIndex)

        Gauss_Jordan.gauss_jordan(maxIndex, minIndex, matrix, rightSide)
        if maxResult < -rightSide[0]:
            maxResult = -rightSide[0]


def make_solution(matrix, maxResult, basis, rightSide):
    print("Maximum of function is: " + str(round(maxResult)))

    basis.sort()

    for i in range(1, len(matrix)):
        for j in basis:
            if matrix[i][j] == 1:
                print("x with index: " + str(j+1) + " = " + str(round(rightSide[i])))
                break

