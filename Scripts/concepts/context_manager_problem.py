# # The above code will open 100000 file descriptors and will not close them.
# # This will lead to resource leak.
# file_descriptors = []
# for x in range(100000):
#     file_descriptors.append(open('test.txt', 'w'))
#
# # Output:
# # OSError: [Errno 24] Too many open files: 'test.txt'

file_descriptors = []
for x in range(100000):
    with open("test.txt") as f:
        data = f.read()
