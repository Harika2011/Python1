def check_age():
    while True:
        try:
            age = int(input("Enter your age (enter a negative number to exit): "))
            
            if age < 0:
                print("Exiting the program. Goodbye!")
                break
            
            if age > 110:  
                print("Error: The age entered seems unrealistic.")
            else:
                if age % 2 == 0:
                    print(f"The age {age} is even.")
                else:
                    print(f"The age {age} is odd.")
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for age.")

check_age()
