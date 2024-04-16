# find second max element in list
my_range = 100
l1 = range(my_range)

# using sort
l1.sort()   # O(nlogn)
print("Second max element using sort:", l1[-2])

# using set
l1 = list(set(l1))
l1.sort()   # O(n)
print("Second max element using set:", l1[-2])

# using max function
max_ele = max(l1)
l1.remove(max_ele)
print("Second max element using max function:", max(l1))

# using list comprehension
max_ele = max(l1)
l1 = [i for i in l1 if i != max_ele]
print("Second max element using list comprehension:", max(l1))

# using for loop
max_ele = max(l1)
second_max = l1[0]
for i in l1:
    if i > second_max and i != max_ele:
        second_max = i
print("Second max element using for loop:", second_max)

# using binary search
def find_second_max(l1):
    max_ele = l1[0]
    second_max = l1[0]
    for i in l1:
        if i > max_ele:
            second_max = max_ele
            max_ele = i
        elif i > second_max and i != max_ele:
            second_max = i
    return second_max

# using collections
from collections import Counter
l1 = Counter(l1)
print("Second max element using collections:", l1.most_common(2)[-1][0])

# using itertools
import itertools
l1 = itertools.permutations(l1, 2)
print("Second max element using itertools:", list(l1)[-1][0])



