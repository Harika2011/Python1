class IOString():
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter String : ")

    def print_String(self):
        print("Result is : ", self.str1.upper())

str1 = IOString()

str1.get_string()
str1.print_String()
