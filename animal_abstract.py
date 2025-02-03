from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("Humans can walk and run")

class Dog(Animal):
    def move(self):
        print("Dogs can run and jump.")

class Fish(Animal):
    def move(self):
        print("Fish can swim")

human = Human()
dog = Dog()
fish = Fish()

human.move()
dog.move()
fish.move()
