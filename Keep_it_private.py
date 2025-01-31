class MyClass:
    def __init__(self, value):
        self.__privateVar = value  

    def __privMeth(self):
        print("This is a private method!")

    def hello(self):
        print("Private Variable Value:", self.__privateVar)

    def access_private_method(self):
        self.__privMeth()  


obj = MyClass(42)

obj.hello()

obj.access_private_method()

obj._MyClass__privMeth()  

print("Accessing Private Variable Directly:", obj._MyClass__privateVar)
