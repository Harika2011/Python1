user = input("ENter the elements of the list spereated by spaces: ").split()

print("Your list is ",user)

remove = input("Enter the value u want to remove: ")

if remove in user:
    user.remove(remove)
    print("The updated list upon removing is: ",user)
    new = input ("what new value do u want to add: ")
    replace = int(input(f"Enter the position (0 to {len(user)}) to insert '{new}' "))
    user.insert(replace,new)
    print("The final updated list is: ", user)
else:
    print("Value",remove,"is not found")
