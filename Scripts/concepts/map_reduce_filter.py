aa_list = range(1, 11)

# square of list elements
output_list = map(lambda x: x * x, aa_list)
bb_list = list(output_list)
print(bb_list)

# filter even numbers
even_square = filter(lambda x: x % 2 == 0, bb_list)
print(list(even_square))

# reduce sum of list elements
from functools import reduce
sum_of_list = reduce(lambda x, y: x + y, bb_list)
print(sum_of_list)