string = "Hello isi olleH"

# Convert the string to lowercase
string = string.lower()
mid = len(string) // 2
is_palindrome = True

def isPalindrome(s): # using slicing
    return s == s[::-1]


# function to check string is
# palindrome or not
def isPalindrome(s):
    # Using predefined function to
    # reverse to string print(s)
    rev = ''.join(reversed(s))

def isPalindromeReverse(s):
    # Checking if both string are
    # equal or not
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False

# Check if the given string is a palindrome
for i in range(mid):
    if string[i] != string[-i-1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")


# Using the isPalindrome function
if isPalindrome(string):
    print("The given string is a palindrome check using function")
else:
    print("The given string is not a palindrome check using function")


# Using the isPalindrome function
if isPalindromeReverse(string):
    print("The given string is a palindrome check using function reverse")
else:
    print("The given string is not a palindrome check using function reverse")