

import SimplexMethod


matrix = [[8, 6, 0, 0, 0],
          [1, 4, 1, 0, 0],
          [2, 1, 0, 1, 0],
          [0, 1, 0, 0, 1]]

rightSide = [0,2048, 2048, 480]
SimplexMethod.simplex(matrix,rightSide)

