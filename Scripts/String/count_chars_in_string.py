# input AAAABBBCCDAA
# output 4A3B2C1D2A

# Python code to count the number of characters in a string
my_string = "AAAABBBCCDAA"
result = ""
count = 1
for i in range(len(my_string)-1):
    if my_string[i] == my_string[i + 1]:
        count += 1
    else:
        result += str(count) + my_string[i]
        count = 1
result += str(count) + my_string[-1]

print(result)



