def calculate_product(numbers_tuple):
   
    product = 1
    for number in numbers_tuple:
        product *= number
    return product

def main():
    print("Welcome to the Tuple Product Calculator!")
    print("Enter the elements of the tuple separated by spaces (e.g., 2 3 4):")
    
    try:
        user_input = input("Enter your tuple elements: ")
        numbers_tuple = tuple(map(int, user_input.split()))
        
        if not numbers_tuple:
            print("The tuple is empty. No product to calculate.")
        else:
            product = calculate_product(numbers_tuple)
            print(f"The product of the numbers in the tuple {numbers_tuple} is {product}.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

main()
