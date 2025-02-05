class Flashcard:
    def __init__(self,word,definition):
        self.word = word
        self.definition = definition

    def __str__(self):
        return f"Word: {self.word}\nDefinition: {self.definition}"
    

def create_flashcards():
    flashcards = []

    while True:
        word = input("Enter the word (or type 'exit' to stop):")

        if word.lower() == 'exit':
            break

        definition = input(f"Enter the definition of '{word}'")

        flashcard = Flashcard(word,definition)
        flashcards.append(flashcard)

    print("\n Here are all your flashcards: ")
    index = 0
    while index < len(flashcards):
        print(flashcards[index])
        print("-"* 50)
        index += 1

create_flashcards()
