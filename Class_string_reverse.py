
#Write a Python class to reverse a string word by word.



class StringReverser:
    def __init__(self, text):
        self._protected_text = text  
        self.__private_text = self._reverse_words()  

    def _reverse_words(self):
        
        return ' '.join(self._protected_text.split()[::-1])

    def get_reversed_string(self):
        
        return self.__private_text

sentence = "Hello world this is Python"
reverser = StringReverser(sentence)
print(reverser.get_reversed_string())  


print(reverser._StringReverser__private_text) 
