# Python code
# To reverse words in a given string

# input string
string = "geeks quiz practice code"
# reversing words in a given string
#  using slicing
s = string.split()[::-1]
print(" ".join(s))


# using reversed function
a = string.split()
print(" ".join(reversed(a)))

l = []
for i in s:
    # appending reversed words to l
    l.append(i)
# printing reverse words
print(" ".join(l))