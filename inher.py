class Person:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age)
        self.student_id = student_id

class Staff(Person):
    def __init__(self, pid, name, age, staff_id):
        super().__init__(pid, name, age)
        self.staff_id = staff_id

student = Student(1234567890123, "Alice", 20, "s123")
staff = Staff(2345678901234, "Bob", 25), "s234"
print(f"S : {student.name}, age : {student.age}, id : {student.student_id}")
print(f"S : {staff.name}, age : {staff.age}, id : {staff.staff_id}")

