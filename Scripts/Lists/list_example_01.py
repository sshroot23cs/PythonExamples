A1 = [2, 7, 5, 6, 8, 11, 12, 3, 4]
A2 = [12, 17, 15, 6, 8, 1, 4, 3, 7]

# find the common elements in the two lists
# using 2 for loop
common_elements = []
for i in A1:
    for j in A2:
        if i == j:
            common_elements.append(i)
            break
print(common_elements)

# using 1 for loop
common_elements = []
for i in A1:
    if i in A2:
        common_elements.append(i)
print(common_elements)

# using list comprehension
common_elements = [i for i in A1 for j in A2 if i == j]
print(common_elements)

# using set intersection
common_elements = list(set(A1).intersection(A2))
print(common_elements)


