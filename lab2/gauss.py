import math
import cmath
from copy import copy, deepcopy
from re import A
import numpy as np

def solveMatrixGaussMaxEl(A, B):

        def deleteRowAndCol(rowIndex, colIndex):
            poppedRow = copy(initialMatrix[rowIndex])
            poppedSol = initialSol[rowIndex]
            deletedInitialRows.append(copy(poppedRow))
            deletedInitialSol.append(poppedSol)

            for colJ in range(len(poppedRow)):
                poppedRow[colJ] /= maxEl
                
            poppedSol /= maxEl

            for rowI in range(len(initialMatrix)):
                initialMatrix[rowI][colIndex] = 0
                
            initialMatrix.pop(rowIndex)
            initialSol.pop(rowIndex)

            finalSol.append(poppedSol)
            finalMatrix.append(copy(poppedRow))

        def changeElements():
            for rowI in range(len(initialMatrix)):
                initialSol[rowI] += deletedInitialSol[steps - 1] * mList[steps - 1][rowI]
                for colJ in range(len(initialMatrix[rowI])):
                    initialMatrix[rowI][colJ] += (deletedInitialRows[steps - 1][colJ] * mList[steps - 1][rowI]) \
                        if abs(initialMatrix[rowI][colJ]) != 0 else 0

        def findMaxAbs():
            maxElement = initialMatrix[0][0]
            rowIndex = 0
            colIndex = 0
            for rowI in range(len(initialMatrix)):
                for colJ in range(len(initialMatrix[rowI])):
                    if abs(maxElement) < abs(initialMatrix[rowI][colJ]):
                        maxElement = initialMatrix[rowI][colJ]
                        rowIndex = rowI
                        colIndex = colJ
            return rowIndex, colIndex, maxElement

        initialMatrix = deepcopy(A)
        initialSol = list(copy(B))
        finalMatrix = []
        finalSol = []
        deletedInitialRows = []
        deletedInitialSol = []
        mList = []
        
        for steps in range(len(A)):
            tempMList = []
            if steps != 0:
                changeElements()
            rowD, colD, maxEl = findMaxAbs()
            for i in range(len(initialMatrix)):
                if i != rowD:
                    mi = -(initialMatrix[i][colD] / maxEl)
                    tempMList.append(mi)
            deleteRowAndCol(rowD, colD)

            mList.append(copy(tempMList))
            tempMList.clear()

        return returnSolution(finalMatrix, finalSol)
    
    
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

    
    my = solveMatrixGaussMaxEl(A, B)
    numpy = numpySolution(A, B)
    
    print(my)
    print(numpy)
    printE(my, numpy)
        
if __name__ == '__main__':
    main()