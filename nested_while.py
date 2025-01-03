def nested():
    while True:
        try:
            num= int(input("Enter a num(Enter a negative num to quit)"))
            if num < 0:
                print("Bye Bye! I am leaving!!")
                break
            while num%2 == 0:
                print("The number si divisible by 2.Bye! Starting the infinite loop")
                while True:
                    print("Bye")
        except ValueError:
            print("The number you entered is not an integer")

nested()
