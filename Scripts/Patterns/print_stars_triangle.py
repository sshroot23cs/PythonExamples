max_no_of = 11
mid = max_no_of + 1

# print right-angled triangle of stars
# for i in range(max_no_of+1):
#     print("* "*i)
#
# # print isosceles triangle of stars
# for i in range(max_no_of+1):
#     print(" "*mid + "* "*i)
#     mid = mid - 1
# # print inverted isosceles triangle of stars

for i in range(max_no_of, 0, -1):
    print(" "*mid + "* "*i)
    mid = mid + 1

# for i in range(max_no_of):
#     print(" "*(max_no_of-i-1) + "* "*(i+1))



