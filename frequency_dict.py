test_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 1
}

value_to_check = 1

frequency = list(test_dict.values()).count(value_to_check)

print(f"The frequency of {value_to_check} is: {frequency}")
