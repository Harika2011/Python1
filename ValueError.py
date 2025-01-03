try:
    number = int(input("Enter a num"))
    print("The number is ",number)
except ValueError as ex:
    print("Exception",ex)
