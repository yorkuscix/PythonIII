# when a function calls itself, it's called recursion
# trace this code and try to figure out what it does

def f(word: str):
    if len(word) == 1:
        return word
    else:
        return f(word[:-1])