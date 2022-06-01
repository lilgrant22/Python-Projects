import unittest

import os

from src import declaration


class TestDeclarationMethods(unittest.TestCase):
    """
        Test Class for small_data.py
    """

    def setUp(self):
        self.declaration_file = os.path.join("data", "declaration.txt")
        self.letter_file = os.path.join("data", "student_letter.txt")
        self.fellowship_file = os.path.join("data", "fellowship.txt")


    def test_read_declaration(self):
        expected = {'I': 455, 'N': 490, 'C': 187, 'O': 518, 'G': 131, 'R': 429, 'E': 868, 'S': 483, ',': 107, 'J': 17, 'U': 213,
         'L': 230, 'Y': 82, '4': 1, '1': 1, '7': 2, '6': 1, '.': 37, 'T': 648, 'H': 352, 'A': 483, 'M': 146, 'D': 254,
         'F': 182, 'W': 97, 'V': 74, 'B': 95, 'P': 138, 'Q': 6, "'":1, 'K':14, '-':7, 'Z':4, ';':10, 'X':9, ':':9, '&':1 }
        exp_cnt = 6782 # Don't count spaces, tabs, or newlines
        with open(self.declaration_file) as letter:
            text = letter.readlines()  # Read entire file into a list of strings
        hist, count = declaration.calc_histogram(text)

        self.assertEqual(exp_cnt, count, msg="Total non-whitespace character count does not match! Don't count spaces, tabs, or newlines.")
        self.assertEqual(expected, hist, msg="Histogram dictionary is not correct ")

    def test_read_letter(self):
        expected = {'D':16, 'E':57, 'A':25, 'R':44, 'S':38, 'T':47, 'U':35, 'N':29, ',':6,
                    'Y':22, 'O':66, 'H':18, 'L':23, 'W':12, 'K':11, 'P':13, 'C':23, 'I':29,
                    'G':15, 'M':12, '.':10, 'B':9, '(':2, ')':2, 'F':11, 'X':2, 'Z':1, 'J':1,
                    '-':1, 'V':3, ';':1, "'":1, '2':1, '5':1, '0':1, }

        exp_cnt = 588 # Don't count spaces, tabs, or newlines
        with open(self.letter_file) as letter:
            text = letter.readlines()  # Read entire file into a list of strings
        hist, count = declaration.calc_histogram(text)
        # ans = "{"
        # for key, val in hist.items():
        #     ans += "'{}':{}, ".format(key, val)
        # ans += "}"
        # print(ans)

        self.assertEqual(exp_cnt, count, msg="Total non-whitespace character count does not match! Don't count spaces, tabs, or newlines.")
        self.assertEqual(expected, hist, msg="Histogram dictionary is not correct ")


    def test_read_fellowship(self):
        expected = {'F':2, 'R':7, 'O':6, 'D':2, 'B':2, 'A':8, 'G':8, 'I':7,
                    'N':4, 'S':4, 'M':5, 'W':1, 'E':5, 'L':4, 'P':3, 'Y':1, }

        exp_cnt = 69 # Don't count spaces, tabs, or newlines
        with open(self.fellowship_file) as letter:
            text = letter.readlines()  # Read entire file into a list of strings
        hist, count = declaration.calc_histogram(text)
        ans = "{"
        for key, val in hist.items():
            ans += "'{}':{}, ".format(key, val)
        ans += "}"
        print(ans)

        self.assertEqual(exp_cnt, count, msg="Total non-whitespace character count does not match! Don't count spaces, tabs, or newlines.")
        self.assertEqual(expected, hist, msg="Histogram dictionary is not correct ")


if __name__ == '__main__':
    unittest.main()
