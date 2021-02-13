file = open("seuss-green-eggs-short.txt")
all_text = []
for line in file:
    line_words = line.split()
    for word in line_words:
        all_text.append(word.lower())
