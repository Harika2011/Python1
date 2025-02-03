#Write a Python program to create two classes - BMW and Ferrari with similar methods and implement Polymorphism on them.


class BMW:
    def start_engine(self):
        return "BMW engine started with a smoothhhhhhh roarrrrrr."

    def top_speed(self):
        return "The BMW has a top speed of 250 km/h."

    def price(self):
        return "The BMW costs around 1.82 Crore."

class Ferrari:
    def start_engine(self):
        return "Ferrari engine started with a louddddddddddddd revvvvvvv."

    def top_speed(self):
        return "The Ferrari has a top speed of 350 km/h."

    def price(self):
        return "The Ferrari costs around  3.50 Crore"

def car_details(car):
    print(car.start_engine())
    print(car.top_speed())
    print(car.price())
    print("-" * 100)

bmw_car = BMW()
ferrari_car = Ferrari()

car_details(bmw_car)
car_details(ferrari_car)
