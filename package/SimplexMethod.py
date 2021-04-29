def output(list):
    for i in list:
        for j in i:
            print(j, end="   ")
        print()
    print()


def simplex(matrix, rightSide):

    basis = [[0 for j in range(len(rightSide)-1)] for i in range(len(rightSide)-1)]

    numberOfValue = [i for i in range(len(matrix[0])-len(rightSide)+2, len(matrix[0])+1)]

    for i in range(len(rightSide)-1):
        basis[i][i] = 1

    output(basis)

    max = 0

    for i in range(len(matrix[0])):
        if max > matrix[0][i] > 0:
            max = matrix[0][i]

