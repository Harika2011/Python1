#Write a program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breeds.

class Dog:
    species = "Canis lupus familiaris" 

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 31)

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("German Shepherd", "German")

print("Dog 1 Details:")
dog1.display_details()

print("Dog 2 Details:")
dog2.display_details()
