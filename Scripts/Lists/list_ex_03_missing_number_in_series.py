# find missing number in series
num_list = [1, 2, 3, 4, 5, 6, 8, 9, 10]
max_num = max(num_list)

# using for loop
for i in range(1, max_num):
    if i not in num_list:
        print("Missing number:", i)

# using list comprehension
missing_num = [i for i in range(1, max_num) if i not in num_list]
print("using list comprehension", missing_num)

# using set difference
missing_num = list(set(range(1, max_num)) - set(num_list))
print("using set", missing_num)

missing_num = set(range(1, max_num)).difference(num_list)
print("using set", missing_num)

# number sum logic
max_num = 10
sum_num = max_num * (max_num + 1) / 2
print("missing number using sum logic:", sum_num - sum(num_list))

