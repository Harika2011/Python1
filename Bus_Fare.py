class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 10 


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()  
        maintenance_charge = base_fare * 0.10  
        return base_fare + maintenance_charge



bus = Bus(10)  
print("Total Bus Fare: ",bus.fare())  
