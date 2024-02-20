
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
d = {}
for sentence in sentences:
    # counting number of times each word comes
    for word in sentence.split():
        word = word.strip('.,!?":;()[]{}')
        d[word] = d.get(word, 0) + 1

pprint.pprint(d)

