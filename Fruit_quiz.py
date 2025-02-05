import random

class FruitQuiz:
    def __init__(self):
        self.fruit_colors = {
            "Apple": "Red",
            "Banana": "Yellow",
            "Grapes": "Purple",
            "Orange": "Orange",
            "Lemon": "Yellow",
            "Watermelon": "Green",
            "Blueberry": "Blue",
            "Strawberry": "Red",
            "Kiwi": "Brown",
            "Peach": "Pink"
        }

    def start_quiz(self):
        fruit, correct_color = random.choice(list(self.fruit_colors.items()))

        print(f"Guess the color of the fruit: {fruit}")
        user_answer = input("Enter the color: ").strip().capitalize()

        if user_answer == correct_color:
            print("Correct! Well done.")
        else:
            print(f"Oops! The correct color of {fruit} is {correct_color}.")


if __name__ == "__main__":
    quiz = FruitQuiz()
    quiz.start_quiz()
    


