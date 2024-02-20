string = "Hello isi olleH"

mid = len(string) // 2
is_symmetrical = True

# Check if the given string is symmetrical
for i in range(mid):
    if string[i] != string[mid + i]:
        is_symmetrical = False
        break

if is_symmetrical:
    print("The given string is symmetrical")
else:
    print("The given string is not symmetrical")