def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    square_values = [x ** 2 for x in range(start, end + 1)]

    even_values = [value for value in square_values if value % 2 == 0]
    odd_values = [value for value in square_values if value % 2 != 0]

    print("Squares of numbers in range" ,start,"and",end,"is",square_values)
    print("Even square values:" ,even_values)
    print("Odd square values:", odd_values)

main()
