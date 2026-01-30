from models.classroom import Classroom
from models.student import Student


oop = Classroom("OOP")
oop.add_student(Student(1, "Alice", 20, "s001"))
oop.add_student(Student(2, "Bob", 21, "s002"))
print(f"{oop.name} registered {len(oop)} students")
oop.add_student(Student(3, "Charlie", 22, "s003"))
print(len(oop))
print('Students in classroom:')
for i in range(len(oop)):
    print(oop[i])