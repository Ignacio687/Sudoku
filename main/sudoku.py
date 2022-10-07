
class NumberAlreadyInRowException(Exception):
    pass

class NumberAlreadyInColumnException(Exception):
    pass

class NumberAlreadyInSectorException(Exception):
    pass

class Sudoku():
    def __init__(self, table):
        self.table = table
        self.originalTable = table

    def add(self, number, row, col):
        for rowValue in self.table[row]:
            if rowValue == number:
                raise NumberAlreadyInRowException 
        for rowCounter in self.table:
            if rowCounter[col] == number:
                raise NumberAlreadyInColumnException
        #Set row and col to the row/col start value of the respective sector:
        #sSR = sectorStartRow
        sSR = row
        if sSR/3 != sSR//3:
            sSR = sSR-1 if sSR/3 < sSR//3+0.3 else sSR-2
        #sSC = sectorStartcol
        sSC = col
        if sSC/3 != sSC//3:
            sSC = sSC-1 if sSC/3 < sSC//3+0.3 else sSC-2
        for rowCounter in range(sSR, sSR+3):
            for colCounter in range(sSC, sSC+3):
                if self.table[rowCounter][colCounter] == number:
                    raise NumberAlreadyInSectorException
        self.table[row][col] = number

    def reset(self):
        self.table = self.originalTable