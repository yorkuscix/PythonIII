import random

class Word:
    def __init__(self, text):
        self.text = text
        self.possible_next = []
    
    def __str__(self):
        return self.text + ": " + str(self.possible_next)
    
    def add_next(self, new_text):
        self.possible_next.append(new_text)
    
    def random_next(self):
        count = len(self.possible_next)
        rand = random.randint(0, count-1)
        return self.possible_next[rand]

class Dictionary:
    def __init__(self):
        self.words = []
    
    def __str__(self):
        result = ''
        for word in self.words:
            result = result + str(word) + ", "
        return result