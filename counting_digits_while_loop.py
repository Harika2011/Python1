number = input("Enter a number")

number = abs(int(number))

digit = 0 

while number>0:
    number//= 10 
    digit += 1

print ("The total num of digits is",digit)
