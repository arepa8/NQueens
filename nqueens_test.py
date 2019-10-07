"""
	Unit Test for NQueens
	@author: Andres Hernandez
"""

import pytest

from nqueens import NQueens

class TestClass:
    def test_n_one(self):
        x = NQueens(1)
        assert x.solutions == 1


    def test_n_two(self):
        x = NQueens(2)
        assert x.solutions == 0


    def test_n_three(self):
        x = NQueens(3)
        assert x.solutions == 0


    def test_n_four(self):
        x = NQueens(4)
        assert x.solutions == 2


    def test_n_five(self):
        x = NQueens(5)
        assert x.solutions == 10


    def test_n_six(self):
        x = NQueens(6)
        assert x.solutions == 4


    def test_n_seven(self):
        x = NQueens(7)
        assert x.solutions == 40


    def test_n_eight(self):
        x = NQueens(8)
        assert x.solutions == 92


    def test_n_nine(self):
        x = NQueens(9)
        assert x.solutions == 352


