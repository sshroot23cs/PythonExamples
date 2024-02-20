given_string = "Hello, World!"

# Reverse the given string
reversed_string = given_string[::-1]
# Print the reversed string
print(reversed_string)

# Reverse the reversed string without using slicing and reverse function
reversed_string = ""
for char in given_string:
    reversed_string = char + reversed_string

print(reversed_string)


