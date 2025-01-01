a = input("Enter a word of your choice: ")

found = False  
for char in a:
    if char == 'a':
        found = True
        break  

if found:
    print("a is found")
else:
    print("a is not found")
