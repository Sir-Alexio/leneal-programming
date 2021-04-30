import Gauss_Jordan

def output(list):
    for i in list:
        for j in i:
            print(j, end="   ")
        print()
    print()


def simplex(matrix, rightSide):
    basis = [[0 for j in range(len(rightSide) - 1)] for i in range(len(rightSide) - 1)]

    numberOfValue = [i for i in range(len(matrix[0]) - len(rightSide) + 2, len(matrix[0]) + 1)]

    for i in range(len(rightSide) - 1):
        basis[i][i] = 1

    print(numberOfValue)
# ------------------------------------------------------------
    max = 0

    maxIndex = 0

    for i in range(len(matrix[0])):  # условие оптимальности
        if max > matrix[0][i] > 0:
            max = matrix[0][i]
            maxIndex = i

    if max == 0:  # условие выхода
        return False

# -----------------------------------------------------------
    minimum = rightSide[1]

    minIndex = 0

    for i in range(1,len(rightSide)):
        result = rightSide[i]/matrix[i][maxIndex]
        if minimum<result:
            minimum = result
            minIndex = i

    Gauss_Jordan.gauss_jordan(maxIndex, minIndex,matrix,rightSide)

