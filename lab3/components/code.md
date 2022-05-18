Алгоритм реализован на языке **Python**:


```python
import math
import cmath
from copy import copy, deepcopy
import numpy as np


def solveMatrixOptimalException(A,B):

        def upSum(nArray, oArray, kIndex, jIndex):
            total = 0
            for index in range(kIndex):
                total += nArray[index][jIndex] * oArray[kIndex][index]
            return total

        initialMatrix = deepcopy(A)
        initialSol = list(copy(B))

        n = len(initialMatrix)

        finalMatrix = []
        for i in range(n):
            finalMatrix.append([*initialMatrix[i], initialSol[i]])

        A_B = deepcopy(finalMatrix)

        major = finalMatrix[0][0]
        for i in range(n + 1):
            finalMatrix[0][i] /= major

        for k in range(1, n):

            for j in range(k + 1, n + 1):
                s1 = upSum(finalMatrix, A_B, k, j)
                s2 = upSum(finalMatrix, A_B, k, k)
                finalMatrix[k][j] = (A_B[k][j] - s1) / (A_B[k][k] - s2)

            for i in range(k - 1, -1, -1):
                for j in range(k + 1, n + 1):
                    finalMatrix[i][j] = finalMatrix[i][j] - finalMatrix[k][j] * finalMatrix[i][k]

            for i in range(k):
                finalMatrix[i][k] = 0
                finalMatrix[k][i] = 0

            finalMatrix[k][k] = 1

        matr = []
        sol = []
        for i in range(len(finalMatrix)):
            matr.append(finalMatrix[i][:len(finalMatrix)])
            sol.append((finalMatrix[i][len(finalMatrix)]))

        return returnSolution(matr, sol)

def numpySolution(givenMatrix, givenSolution):
    return np.linalg.solve(givenMatrix, givenSolution)


def returnSolution(finalMatrix, finalSol):
    rootsList = [0] * len(finalMatrix[0])
    for equationI in reversed(range(len(finalMatrix))):
        tempRoot = finalSol[equationI]
        indexOfRoot = 0
        if equationI == len(finalMatrix) - 1:
            for rootJ in range(len(finalMatrix[equationI])):
                if finalMatrix[equationI][rootJ] != 0:
                    indexOfRoot = rootJ
                    rootsList[indexOfRoot] = tempRoot
        else:
            for rootJ in range(len(finalMatrix[equationI])):
                if finalMatrix[equationI][rootJ] != 0 and rootsList[rootJ] == 0:
                    indexOfRoot = rootJ
            for rootJ in range(len(finalMatrix[equationI])):
                if finalMatrix[equationI][rootJ] != 0 and rootJ != indexOfRoot:
                    tempRoot -= rootsList[rootJ] * finalMatrix[equationI][rootJ]
            rootsList[indexOfRoot] = tempRoot

    return rootsList


def printE(myX, pythonX):
    for i in range(len(myX)):
        print("E" + str(i) + " = ", end="")
        print(abs(pythonX[i] - myX[i]))
    print("\n")

    
def main():
        
    A = [
        [0.411, 0.421, -0.333, 0.313, -0.141, -0.381, 0.245],
        [0.241, 0.705, 0.139, -0.409, 0.321, 0.0625, 0.101],
        [0.123, -0.239, 0.502, 0.901, 0.243, 0.819, 0.321],
        [0.413, 0.309, 0.801, 0.865, 0.423, 0.118, 0.183],
        [0.241, -0.221, -0.243, 0.134, 1.274, 0.712, 0.423],
        [0.281, 0.525, 0.719, 0.118, -0.974, 0.808, 0.923],
        [0.246, -0.301, 0.231, 0.813, -0.702, 1.223, 1.105]]
    
    B = [0.096, 1.252, 1.024, 1.023, 1.155, 1.937, 1.673]

    
    my = solveMatrixOptimalException(A, B)
    numpy = numpySolution(A, B)
    
    print(my)
    print(numpy)
    printE(my, numpy)
        
if __name__ == '__main__':
    main()

```