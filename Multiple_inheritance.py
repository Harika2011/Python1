
class Person:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class CourseStudent(Person, Course):
    def __init__(self, name, course_name):
        Person.__init__(self, name)
        Course.__init__(self, course_name)

    def enroll(self):
        print(f"{self.name} has enrolled in {self.course_name}")

student = CourseStudent("Harika", "Python Programming")
student.enroll()  
