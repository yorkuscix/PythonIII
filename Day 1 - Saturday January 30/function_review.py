# <-- this is a comment. Python ignores everything after

# counts the number of upper and lower case A's in a word
def a(word: str):
    total = 0
    for letter in word:
        if letter == 'a' or letter == 'A':
            total = total + 1
    return total

# calculates the sum of a list of numbers
def s(new_lst: list):
    total = 0
    for i in new_lst:
        total = total + i
    return total

# calculates the factorial of a number
# notice that the function calls itself on the last line. Trace the code with the example fact(5)
def fact(n: int):
    if n==0:
        return 1
    return n * fact(n-1)
