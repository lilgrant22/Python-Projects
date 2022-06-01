"""
Use this file as a 'factory' to build our instances of Person, ... StudentWorker,
 and test some operations
"""
# pylint: disable-msg=C0103

import math

from given.cnu_person import CNUPerson
from given.person import Person
from given.student import Student
from given.student_worker import StudentWorker

hopper = Person("Grace", "M.", "Hopper")
print(hopper)
print(id(hopper))

person = Person("Manuel", "A.", "P\xE9rez", "Qui\xF1ones")
print(person)

person2 = Person("Grace", "M.", "Hopper")
print("id2=", id(person2))
print(person == hopper)
print(person2 == hopper)
print(person2 is hopper)

hopper2 = Person("Dennis", "Lee", "Hopper")

ptrib = CNUPerson("Paul", "", "Trible", 1)
print("PTrib", ptrib)

provost = CNUPerson("Dave", "", "Doughty", 2)
print(provost)

dean = CNUPerson("Nicole", "R.", "Guajardo", 3)
print(dean)

dept = CNUPerson("Toni", "", "Riedl", 4)
print(dept)
print(type(dept))
print("is type Person? ", type(dept) == Person)
print("is type CNUPerson? ", type(dept) == CNUPerson)
print("is instance of Person? ", isinstance(dept, Person))
print("is instance of CNUPerson? ", isinstance(dept, CNUPerson))


stu1 = Student("Captain", "Chris", "Newport", 0, math.pi)
print(stu1)

stu2 = Student("Joe", "Party", "Hard", 42, 2.001)
print(stu2)

stu2 = Student("Joe", "Party", "ReallyHard", 42, 0.900)
print(stu2)

stu3 = StudentWorker("Suzie", "Study", "Much", 50, 3.900, 10.25)
print(stu3)

stu4 = StudentWorker("John", "Extra", "Work", 51, 2.900, 10.25)
print(stu4)

people = [stu3, stu4, Person("Miguel", "", "P\xE9rez"), hopper, person,
          Person("Dario", "", "P\xE9rez", "Flores"), hopper2,
          Person("N\xE9ster", "Luis", "P\xE9rez", "Luzardo"),
          person2, Person("Isaac", "Tatum", "Hopper"), Person("Thomas", "Edward", "Hopper"),
          Person("Chief", "Jim", "Hopper"),
          ptrib, provost, dean, dept, stu1, stu2]


print("Sorted People:")
sorted_people = people[:].sort()
for person in sorted_people:
    print(person)

print("CNU Persons:")
cnu_persons = None # Get a list of only CNU people

for person in cnu_persons:
    print(person)

print("CNU Students:")
cnu_students = None # Get a list of only CNU people

for person in cnu_students:
    print(person)
