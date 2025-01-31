class Computer:
    def __init__(self, price):
        self.__max_price = price  

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def setMaxPrice(self, new_price):
        if new_price > 0:  
            self.__max_price = new_price
            print("Price updated successfully!")
        else:
            print("Invalid price! Price must be positive.")

comp = Computer(1000)


comp.sell()

comp.__max_price = 2000  
comp.sell()  

comp.setMaxPrice(2000)

comp.sell()

print("Accessing Private Variable Directly:", comp._Computer__max_price)
