import math
import numpy as np


class Sudoku:
    def __init__(self, ):
        self.matrix = np.zeros((9, 9))
        self.list_numbers = list(range(1, 10))

    def show_matrix(self,):
        print("=== Show Matrix ===")
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                print(i, j, end=" ")
            print("")


partida = Sudoku()

# partida.show_matrix()
print(partida.matrix[0])
