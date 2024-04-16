# unsorted list of numbers
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# using for loop

for i in range(len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

# list sorting algorithm
print("using for loop:", l1)
# using sort
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l1.sort()
print("using sort:", l1)
# using sorted
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("using sorted:", sorted(l1))
# using min and remove
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l2 = []
for i in range(len(l1)):
    min_ele = min(l1)
    l2.append(min_ele)
    l1.remove(min_ele)


print("using min and remove:", l2)

# using min and list comprehension
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l2 = []
for i in range(len(l1)):
    l2.append(min(l1))
    l1 = [x for x in l1 if x != min(l1)]
print("using min and list comprehension:", l2)

# using min and while loop
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l2 = []
while l1:
    min_ele = min(l1)
    l2.append(min_ele)
    l1.remove(min_ele)

print("using min and while loop:", l2)

# using min and while loop
l1 = [120, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l2 = []
while l1:
    l2.append(min(l1))
    l1 = [x for x in l1 if x != min(l1)]

print("using min and while loop:", l2)


