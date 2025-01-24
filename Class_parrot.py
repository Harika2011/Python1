class Parrot:
    species = "Bird"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

parrot1 = Parrot("Polly", 5)
parrot2 = Parrot("Blue",3)

print("Parrot is a ", Parrot.species)

print(f"{parrot1.name} is {parrot1.age} years old.")
print(f"{parrot2.name} is {parrot2.age} years old.")
