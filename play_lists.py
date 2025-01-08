def play():
    numbers = input("ENter a list of numbers sperated by spaces ").split()
    numbers = [int(num) for num in numbers]
    total_sum = sum(numbers)
    average = total_sum/len(numbers)
    largest = max(numbers)
    smallest = min(numbers)
    print("The sum of all the numbers is ",total_sum)
    print("The average of all the numbers is ",average)
    print("The largest of all the numbers is ",largest)
    print("The smallest of all the numbers is ",smallest)

play()

