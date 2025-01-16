data = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

def check_value_frequency(dictionary,value):
    frequency = list(dictionary.values()).count(value)
    return frequency

value_to_check = 2
frequency = check_value_frequency(data, value_to_check)

print(f"The value {value_to_check} appears {frequency} times in the dictionary.")

