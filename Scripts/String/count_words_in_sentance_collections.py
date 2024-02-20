from collections import Counter

# initializing string
sentence = 'Gfg is best . Geeks are good and Geeks like Gfg'

# printing original string
print("The original string is : " + str(sentence))

# Words Frequency in String Shorthands
# using Counter() + split()
res = Counter(sentence.split())

# Printing result
print("The words frequency : " + str(dict(res)))
