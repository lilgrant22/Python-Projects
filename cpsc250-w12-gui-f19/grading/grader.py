"""
We define a comboSuite to combine multiple test files into a single test file
to execute.

"""
import unittest
import sys

#from tests import test_student
#from tests import test_employee


def grade():
    suiteList=[]

    #suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_student.TestStudent))
    #suiteList.append(unittest.TestLoader().loadTestsFromTestCase(test_employee.TestEmployee))

    # ----------------   Join them together and run them
    # comboSuite = unittest.TestSuite(suiteList)
    # result = unittest.TextTestRunner(verbosity=1).run(comboSuite)
    #
    # num_errors = len(result.errors)
    # num_failures = len(result.failures)
    # num_skipped = len(result.skipped)
    # num_tests = result.testsRun
    #
    # # Correctness score percentage
    # score = 100.0*(num_tests - (num_errors+num_failures+num_skipped))/num_tests

    # Style checking
    from grading.lint_test import lint_test
    passed1,style1 = lint_test("src/gui_intro.py")
    passed2,style2 = lint_test("src/gui_grid.py")
    passed3,style3 = lint_test("src/helper_gui.py")

    # Convert to percentage points
    style = (style1 + style2 + style3)*(10.0/3.0) # total style in percentage
    if style < 0.0:
        style = 0.0

    grade = style #0.6*score  + 0.4*style

    #print(" Tests={}  errors={} failures={} skipped={} correctness={} style={} Grade={}".format(num_tests, num_errors, num_failures, num_skipped, score, style, grade))
    return grade

if __name__ == "__main__":
    project_grade = grade()
    print(" Final style score = ",project_grade)
