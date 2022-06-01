"""
Demo some reading of student_letter.txt

Modify your Run-Edit Configuration to point to the project folder, not src!
"""

"""
Feel free to define helper methods if you want
"""
import numpy as np
import os
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import string
import collections


def calc_histogram(text):
    """
    Calculate a histogram as a dictionary with non-whitespace characters as keys.

    :param text:
    :return: histogram dictionary and count of non-whitespace characters
    """

    dict = {}
    no_white = 0
    for lines in text:
        if lines.startswith("#"):
            pass
        else:
            upper = lines.upper().strip().replace("\t", "").replace("\n", "").replace(" ", "")
            for letter in upper:
                if letter in dict:
                    dict[letter] += 1
                else:
                    dict[letter] = 1

    for entry in dict:
        no_white += dict[entry]

    return dict, no_white


if __name__ == '__main__':
    import os.path
    file_path = os.path.join("data", 'declaration.txt')
    print(file_path)

    letter = open(file_path)
    text = letter.readlines() # Read entire file into a list of strings
    letter.close()  # If you open it, close it!

    hist, count = calc_histogram(text)

    keys = list(hist.keys())
    keys.sort()
    print("Keys:", keys)
    sum = 0.0
    for a in keys:
        val = 100.0*(hist[a]/count)
        print("{} : {:4d} : {:7.3f}%".format(a, hist[a], val))
        sum += val

    print("total={:.5f}\ncnt={}".format(sum, count))
