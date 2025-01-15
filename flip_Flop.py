def is_palindrome(input_tuple):
   
    return input_tuple == input_tuple[::-1]

def main():
    print("Welcome to the Palindrome Checker for Tuples!")
    print("Enter the elements of the tuple separated by spaces (e.g., 1 2 3 3 2 1):")
    
    user_input = input("Enter your tuple elements: ")
    
    try:
        tuple_elements = tuple(map(int, user_input.split()))
        
        if is_palindrome(tuple_elements):
            print(f"The tuple {tuple_elements} is a palindrome.")
        else:
            print(f"The tuple {tuple_elements} is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter a valid tuple of integers.")


main()
