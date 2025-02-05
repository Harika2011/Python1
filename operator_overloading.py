class CompareValues:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

ob1 = CompareValues(3)
ob2 = CompareValues(4)
ob3 = CompareValues(3)

print(f"ob1 < ob2: {ob1 < ob2}")  
print(f"ob1 == ob2: {ob1 == ob2}")  
print(f"ob1 == ob3: {ob1 == ob3}")  
print(f"ob2 < ob1: {ob2 < ob1}")  
