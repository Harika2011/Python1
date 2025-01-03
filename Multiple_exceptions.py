def exceptions():
    try:
        num1 = int(input("Enter one num"))
        num2 = int(input("Enter another num"))
        result = num1/num2
        print("The result is ",result)
    except ZeroDivisionError:
        print("Division by zero is not possible")
    except SyntaxError:
        print("Not entered the right way")
    except:
        print("Wrong input")
    finally:
        print("Execution of the try-except-finally block is done")

exceptions()
