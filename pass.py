
start = int(input("Enter the starting number in range(smaller value)"))
end = int(input("Enter an ending number to the range(greater value)"))
for num in range(start,end,+1):
    if num % 20 == 0:
        print("twist")
    elif num % 15 == 0:
        pass
    elif num % 5 == 0:
        print("fizz")
    elif num % 3 == 0:
        print("buzz")
    else:
        print("no")

           

