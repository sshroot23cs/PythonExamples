sentance = "This is a sentance with 7 words."

# Split the sentance into words
words = sentance.split()
print(words)
# Print the number of words in the sentance
print(len(words))
# Output:
# ['This', 'is', 'a', 'sentance', 'with', '7', 'words']
# 7
# count duplicate words in a sentance
# Python code to count the number of words in a sentence
# using a dictionary
# input string
string = "Geeks for Geeks."
# initializing dictionary
d = {}
# counting number of times each word comes
for word in string.split():
    d[word] = d.get(word, 0) + 1
print(d)
# Output:
# {'This': 1, 'is': 1, 'a': 1, 'sentance': 1, 'with': 1, '7': 1, 'words': 1}
