# Input : test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}
# Output : {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}

# Write a python program to swap the key and values of the dictionary.
# Expected Output : {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}
test_dict = {'abc' : [10, 30], 'bcd' : [30, 40, 10]}
out_put_dict = {}
for key, value in test_dict.items():
    for ele in value:
        if ele in out_put_dict.keys():
            out_put_dict[ele].append(key)
        else:
            out_put_dict[ele] = [key]

print(out_put_dict)
