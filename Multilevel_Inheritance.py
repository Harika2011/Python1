class University:
    def __init__(self, name):
        self.name = name

    def display_university(self):
        print(f"University: {self.name}")

class Department(University):
    def __init__(self, name, department_name):
        super().__init__(name)
        self.department_name = department_name

    def display_department(self):
        print(f"Department: {self.department_name}")

class Student(Department):
    def __init__(self, name, department_name, student_name):
        super().__init__(name, department_name)
        self.student_name = student_name

    def display_student(self):
        print(f"Student: {self.student_name}")

student = Student("Codingal", "Python Programming", "Harika")
student.display_university()  
student.display_department()  
student.display_student()     
