
from src.class_grade_book import GradeBook
from src.student import Student
from src.course import Course

import csv
import numpy as np
import os

# for names, projects, tests, and quizzes in CRN 9001
names_9001 = []
with open("data/small_test/crn9001/names.txt", "rt") as file:
    lines = file.readlines()
    for line in lines:
        names_9001.append(line)

p_0_list_9001 = []
with open("data/small_test/crn9001/P_0.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        p_0_list_9001.append(line)

p_1_list_9001 = []
with open("data/small_test/crn9001/P_1.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        p_1_list_9001.append(line)

q_0_list_9001 = []
with open("data/small_test/crn9001/Q_0.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        q_0_list_9001.append(line)

q_1_list_9001 = []
with open("data/small_test/crn9001/Q_1.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        q_1_list_9001.append(line)

q_2_list_9001 = []
with open("data/small_test/crn9001/Q_2.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        q_2_list_9001.append(line)

q_3_list_9001 = []
with open("data/small_test/crn9001/Q_3.csv", "rt") as file:
    reader = csv.reader(file)
    for line in reader:
        q_3_list_9001.append(line)
