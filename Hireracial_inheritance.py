class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

class Professor(Person):
    def teach(self):
        print(f"{self.name} is teaching")

class Student(Person):
    def study(self):
        print(f"{self.name} is coding")

professor = Professor("Ms.Renjitha")
student = Student("Harika")
professor.display_name()  
professor.teach()         
student.display_name()    
student.study()           
