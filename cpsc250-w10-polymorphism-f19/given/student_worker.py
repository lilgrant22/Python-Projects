"""
Use this to create StudentWorker class
 @author
 @version
"""
# pylint: disable-msg=C0103


from given.student import Student
from given.employee import Employee


class StudentWorker(Student, Employee):
    def __init__(self, first_name, middle_name, last_name,
                 id, gpa, pay_rate, second_last_name=None):
        Student.__init__(self, first_name, middle_name, last_name,
                         id=id,
                         gpa=gpa, second_last_name=second_last_name)
        Employee.__init__(self, pay_rate)
        self.gpa = gpa

    def __str__(self):
        return Student.__str__(self) + " " + Employee.__str__(self)

