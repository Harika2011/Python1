from abc import ABC, abstractmethod

class BaseClass(ABC):
    def display_value(self, value):
        
        print(f"Value: {value}")

    @abstractmethod
    def abstract_method(self):
        
        pass

class SubClass(BaseClass):
    def abstract_method(self):
        
        print("Abstract method implemented in SubClass")

obj = SubClass()

obj.display_value(10)

obj.abstract_method()
