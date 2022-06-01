"""
Script to handle grade book data

@author <Your Names Here>
@date   <Date Here>
"""

# pylint: disable=C0103

import csv
import numpy as np
import os

def show_files_in_folder(path, prefix=""):
    print(prefix, "Browse folder :", path)
    for data in os.listdir(path):
        full_path = os.path.join(path, data)
        if os.path.isdir(full_path):
            # Call same method again (this is recursion - more later)
            show_files_in_folder(full_path,prefix+"    ") # Add indent to each sub-folder

        elif os.path.isfile(full_path):
            print(prefix, " File > {} ({})".format(data, full_path))
        else:
            print(prefix, " Not a file or directory (folder)! ", data)


if __name__ == '__main__':

    # Demo code to show extracting folder and file names from folder (directory)
    grades_folder = os.path.join("data","small_test")
    show_files_in_folder(grades_folder)

