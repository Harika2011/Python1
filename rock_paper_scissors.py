import random

choices = ["R", "P", "S"]

computer = random.choice(choices)
player = False

while not player:
    player = input("R, P, S? ").upper()  
    
    if player == computer:
        print(f"Tie! Both chose {computer}.")
    elif player == "R":
        if computer == "P":
            print(f"Computer chooses {computer}.")
            print(f"You lose! {computer} covers {player}.")
        else:
            print(f"Computer chooses {computer}.")
            print(f"You win! {player} smashes {computer}.")
    elif player == "P":
        if computer == "S":
            print(f"Computer chooses {computer}.")
            print(f"You lose! {computer} cuts {player}.")
        else:
            print(f"Computer chooses {computer}.")
            print(f"You win! {player} covers {computer}.")
    elif player == "S":
        if computer == "R":
            print(f"Computer chooses {computer}.")
            print(f"You lose! {computer} smashes {player}.")
        else:
            print(f"Computer chooses {computer}.")
            print(f"You win! {player} cuts {computer}.")
    else:
        print("That's not a valid input. Please try again!")
    
    player = False
    computer = random.choice(choices)
