# Input: given_string = “ABC”
# Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”

# Write a python program to generate all the permutations of the given string.

# Approach:
# We will use the itertools module to generate all the permutations of the given string.

# Below is the implementation:
# Python code to generate all the permutations of the given string
from itertools import permutations

# Input: given_string = “ABC”
given_string = "ABC"

# Generate all the permutations of the given string
permutations_list = permutations(given_string)

# Print all the permutations
for permutation in permutations_list:
    print("".join(permutation))

# without using itertools module
# Python code to generate all the permutations of the given string
# Function to generate all the permutations of the given string
def generate_permutations(given_string, start, end):
    # Base case
    if start == end:
        print("".join(given_string))
    else:
        # Generate all the permutations of the given string
        for i in range(start, end + 1):
            # Swap the characters
            given_string[start], given_string[i] = given_string[i], given_string[start]
            # Recursively call the function
            generate_permutations(given_string, start + 1, end)
            # Backtrack
            given_string[start], given_string[i] = given_string[i], given_string[start]


# Input: given_string = “ABC”
given_string = list("ABC")
# Generate all the permutations of the given string
generate_permutations(given_string, 0, len(given_string) - 1)



