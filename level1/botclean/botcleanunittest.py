#!/usr/bin/python
import unittest
import botclean

__author__ = 'njohnson'

CELLS = {0:"-", 1:"d", 2:"b"}

class BotCleanTests(unittest.TestCase):

    def setUp(self):
        # list comprehension
        # initialize 5x5 board to all -
        self.board = [["-" for i in range(5)] for j in range(5)]

    def set_board(self, row0, row1, row2, row3, row4):
        self.board[0] = [CELLS[row0[0]],CELLS[row0[1]],CELLS[row0[2]],CELLS[row0[3]],CELLS[row0[4]]]
        self.board[1] = [CELLS[row1[0]],CELLS[row1[1]],CELLS[row1[2]],CELLS[row1[3]],CELLS[row1[4]]]
        self.board[2] = [CELLS[row2[0]],CELLS[row2[1]],CELLS[row2[2]],CELLS[row2[3]],CELLS[row2[4]]]
        self.board[3] = [CELLS[row3[0]],CELLS[row3[1]],CELLS[row3[2]],CELLS[row3[3]],CELLS[row3[4]]]
        self.board[4] = [CELLS[row4[0]],CELLS[row4[1]],CELLS[row4[2]],CELLS[row4[3]],CELLS[row4[4]]]

    # If on dirty cell, clean
    def test_clean(self):
        posx = 0
        posy = 0
        self.set_board( [1,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0],
                        [0,0,0,0,0])
        self.assertEquals("CLEAN", botclean.decide_move(posx, posy, self.board))

    def test_check_coordinates(self):
        outside_board = [(-1,0),(6,2),(3,-1),(4,6)]
        inside_board = [(0,0),(4,4),(2,3)]

        for coordinate in outside_board:
            self.assertFalse(botclean.check_coordinates(coordinate))

        for coordinate in inside_board:
            self.assertTrue(botclean.check_coordinates(coordinate))

    def test_determine_next_move(self):
        self.assertEquals("RIGHT", botclean.determine_next_move((0,0),(1,0)))
        self.assertEquals("LEFT", botclean.determine_next_move((1,0),(0,0)))
        self.assertEquals("DOWN", botclean.determine_next_move((0,0),(0,1)))
        self.assertEquals("UP", botclean.determine_next_move((0,1),(0,0)))

def main():
    unittest.main()

if __name__ == '__main__':
    main()


