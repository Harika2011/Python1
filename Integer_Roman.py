class RomanConverter:
    def __init__(self):
        self.roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

    def to_roman(self, number: int) -> str:
        if number < 1 or number > 3999:
            raise ValueError("Input must be between 1 and 3999")

        roman_numeral = ""

        for value, symbol in self.roman_map:
            while number >= value:
                roman_numeral += symbol
                number -= value
        
        return roman_numeral

    def from_roman(self, roman: str) -> int:
        roman_map = {symbol: value for value, symbol in self.roman_map}
        roman = roman.upper()
        total = 0
        prev_value = 0

        for char in reversed(roman):
            value = roman_map.get(char)
            if not value:
                raise ValueError(f"Invalid Roman numeral character: {char}")

            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

    def is_valid_roman(self, roman: str) -> bool:
        try:
            self.from_roman(roman)
            return True
        except ValueError:
            return False


def main():
    converter = RomanConverter()
    
    while True:
        print("\nRoman Numeral Converter")
        print("1. Convert integer to Roman numeral")
        print("2. Convert Roman numeral to integer")
        print("3. Check if Roman numeral is valid")
        print("4. Exit")
        
        option = input("Choose an option (1/2/3/4): ")

        if option == "1":
            try:
                num = int(input("Enter an integer (1-3999): "))
                print(f"{num} in Roman numerals is: {converter.to_roman(num)}")
            except ValueError:
                print("Please enter a valid integer.")
        
        elif option == "2":
            roman = input("Enter a Roman numeral: ").strip().upper()
            if converter.is_valid_roman(roman):
                print(f"{roman} is equal to {converter.from_roman(roman)}")
            else:
                print("Invalid Roman numeral.")
        
        elif option == "3":
            roman = input("Enter a Roman numeral to check validity: ").strip().upper()
            if converter.is_valid_roman(roman):
                print(f"{roman} is a valid Roman numeral.")
            else:
                print(f"{roman} is not a valid Roman numeral.")
        
        elif option == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
