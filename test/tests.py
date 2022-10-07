from main.sudoku import *
import unittest

class SudokuTestCase(unittest.TestCase):

    def setUp(self):
        self.table =   [[1, 0, 0, 5, 0, 0, 0, 0, 3],
                        [0, 3, 7, 0, 0, 1, 0, 0, 4],
                        [0, 0, 0, 0, 0, 2, 0, 0, 0],
                        [0, 0, 0, 0, 9, 4, 0, 0, 0],
                        [0, 0, 4, 0, 0, 0, 0, 3, 2],
                        [0, 0, 0, 3, 2, 5, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 2, 0, 0],
                        [7, 4, 0, 0, 0, 0, 0, 0, 0],
                        [8, 0, 0, 0, 0, 3, 1, 0, 0],
                        ]

        self.sudoku = Sudoku(self.table)

        # Table Solved
        #     [1, 8, 9, 5, 4, 7, 6, 2, 3],
        #     [2, 3, 7, 8, 6, 1, 5, 9, 4],
        #     [4, 5, 6, 9, 3, 2, 7, 1, 8],
        #     [3, 2, 1, 6, 9, 4, 8, 5, 7],
        #     [5, 6, 4, 1, 7, 8, 9, 3, 2],
        #     [9, 7, 8, 3, 2, 5, 4, 6, 1],
        #     [6, 1, 3, 4, 8, 9, 2, 7, 5],
        #     [7, 4, 5, 2, 1, 6, 3, 8, 9],
        #     [8, 9, 2, 7, 5, 3, 1, 4, 0],

    def test_addNumber(self):
        self.sudoku.add(8, 0, 1)
        self.assertEqual(self.sudoku.table[0][1], 8)
    
    def test_InsertNumber_NumberAlreadyInRow(self):
        with self.assertRaises(NumberAlreadyInRowException):
            self.sudoku.add(3, 0, 1)

    def test_InsertNumber_NumberAlreadyInColumn(self):
        with self.assertRaises(NumberAlreadyInColumnException):
            self.sudoku.add(9, 2, 4)

    def test_InsertNumber_NumberAlreadyInSector(self):
        with self.assertRaises(NumberAlreadyInSectorException):
            self.sudoku.add(9, 4, 5)

    def test_ResetTable(self):
        self.sudoku.reset()
        self.assertEqual(self.sudoku.table, self.table)

# if __name__ == '__main__':
#     unittest.main()