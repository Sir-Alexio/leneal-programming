import matplotlib as plt


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
