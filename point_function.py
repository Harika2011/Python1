class Point:
    def __init__(self, x, y):
       
        self.x = x
        self.y = y

    def __str__(self):
        
        return f"Point({self.x}, {self.y})"

p1 = Point(10, 15)

print(p1)
