
class Person:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name):
        self.department_name = department_name

class Employee(Person, Department):
    def __init__(self, name, department_name, position):
        Person.__init__(self, name)
        Department.__init__(self, department_name)
        self.position = position

    def work(self):
        print(f"{self.name} works in the {self.department_name} department as a {self.position}.")

emp = Employee("Anjani", "IT", "Engineering manager")
emp.work()  
