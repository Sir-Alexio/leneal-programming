import Gauss_Jordan
import matplotlib.pyplot as plt
import numpy as np


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
            make_solution(matrix, maxResult, basis, rightSide)
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
                print("x with index: " + str(j + 1) + " = " + str(round(rightSide[i])))
                break
    make_grapfic_solution(rightSide)


def make_grapfic_solution(rightSide):
    functions = [lambda x: (2000 - 2 * x) / 6,
                 lambda x: (2048 - x) / 4,
                 lambda x: 2048 - 2 * x,
                 lambda x: 480]

    x = [i for i in range(1024)]

    flag = True
    ax = plt.subplots()

    for f in functions:
        y = [f(i) for i in x]
        if flag:
            plt.plot(x, y, 'b--')
            flag = False
            continue
        plt.plot(x, y)

    plt.plot(rightSide[2], rightSide[1], 'r*')
    plt.grid(True)
    plt.show()
