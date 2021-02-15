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
    
    def get_word(self, text):
        for word in self.words:
            if word.text == text:
                return word
    
    def map(self, from_text, to_text):
        word = self.get_word(from_text)
        if word is None:
            new_word = Word(from_text)
            new_word.add_next(to_text)
            self.words.append(new_word)
        else:
            word.add_next(to_text)

file = open("seuss-green-eggs-long.txt")
all_text = []
for line in file:
    line_words = line.split()
    for word in line_words:
        all_text.append(word.lower())

d = Dictionary()
last_word = ''
for new_word in all_text:
    d.map(last_word, new_word)
    last_word = new_word

def generate_story(start_text, word_data, length):
    story = start_text
    for i in range(length):
        start_word = d.get_word(start_text)
        new_text = start_word.random_next()
        story = story + ' ' + new_text
        start_text = new_text
    return story