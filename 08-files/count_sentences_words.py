# Count lines, sentences, and words in a file.

file = open("random-text.txt")

lines = file.readlines()

print("Lines: ", len(lines))

s = 0
w = 0
for line in lines:
    sentences = line.split('.')
    for sentence in sentences:
        if sentence != '\n':
            s += 1
            words = sentence.split(' ')
            for word in words:
                w += 1
print("Sentences: ", s)
print("Words: ", w)

