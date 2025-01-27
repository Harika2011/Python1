class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo",180,12)
print("Vehicle name:",school_bus.name,"\nSpeed: ",school_bus.max_speed,"\nMileage: ",school_bus.mileage)
