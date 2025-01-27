class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def fly(self):
        print(f"{self.name} can fly!")

    def display(self):
        print(f"Bird Name: {self.name}, Color: {self.color}")

class Penguin(Bird):
    def __init__(self, name, color, species):
        super().__init__(name, color)
        self.species = species

    def swim(self):
        print(f"{self.name}, the {self.species}, can swim!")

    def display_penguin(self):
        print(f"Penguin Name: {self.name}, Color: {self.color}, Species: {self.species}")

penguin = Penguin("Penguin", "Black and White", "Emperor")

penguin.fly()  
penguin.display()  

penguin.swim()
penguin.display_penguin()
