import random
imagine = random.randint(1,100)
name = input("Hi enter ur name")
guesses = 0
print("Hi ,",name,"I am now thinking of a number and you have to guess it are u ready?")

while guesses<19:
    user=int(input("Enter a number"))
    guesses+=1
    if user<imagine:
        print("Your guess is low.Try a bigger num")
    if user>imagine:
        print("your guess is high.Try a smaller num")
    if user==imagine:
        print("you gusses it in ",guesses,"tries")

else:
    print("you didnt guess the right one after 13 attempts.Better luck next tiem and the number was",imagine)
