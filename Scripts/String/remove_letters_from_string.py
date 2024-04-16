str = 'Geeks123For123Geeks4'

# using join() + isdigit() + filter() + lambda
# Remove all digits from a string
res = ''.join(filter(lambda i: i.isalpha(), str))
print(res)

for i in str:
    if i.isalpha():
        print(i, end="")
print()


# check anagram
str1 = "listen"
str2 = "silent"
# using join() + sorted()

# checking anagram
if sorted(str1) == sorted(str2):
    print("Anagram")

