
import os
import pprint
sentences = []
fileName = 'WordCountTextFile.txt'
filePath = os.path.join(os.path.dirname(__file__), "../SampleTextFiles", fileName)
print("Filepath", filePath)
# Open the file in read mode
try:
    with open(filePath) as f:
        for line in f:
            sentences.append(line)
except FileNotFoundError:
    print("File not found")
    exit(1)

# initializing dictionary
# count special characters in a file
special_chars = """[@_!#$%^&*()<>?/|}{~:]".,;'"""
special_chars_list = list(special_chars)
special_chars_count = {}
d = {}
for sentence in sentences:
    # counting number of times each word comes
    for word in sentence.split():
        for char in special_chars_list:
            if char in word:
                if len(word.split(char)) > 2:
                    for i in range(len(word.split(char)) - 1):
                        special_chars_count[char] = special_chars_count.get(char, 0) + 1
                else:
                    special_chars_count[char] = special_chars_count.get(char, 0) + 1
        d[word] = d.get(word, 0) + 1

pprint.pprint(d)
pprint.pprint(special_chars_count)

