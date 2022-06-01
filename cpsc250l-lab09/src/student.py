class Student:

    def __init__(self, first_name, last_name, id, courses, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.courses = courses
        self.gpa = gpa

    def __str__(self):
        return "{} {}, id: {}, course list: {}, GPA: {}".format(self.first_name, self.last_name, self.id, self.courses, self.gpa)