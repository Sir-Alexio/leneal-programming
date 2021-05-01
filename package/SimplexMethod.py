import Gauss_Jordan
import Solution


def output(list):
    for i in list:
        for j in i:
            print(j, end="   ")
        print()
    print()


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
            Solution.make_solution(matrix, maxResult, basis, rightSide)
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

        Gauss_Jordan.gauss_jordan(maxIndex, minIndex, matrix, rightSide)  # Гаус Жордан
        if maxResult < -rightSide[0]:
            maxResult = -rightSide[0]
