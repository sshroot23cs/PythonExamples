size = 8

lines = size # for line

for i in range(size//2+2):
    for j in range(size):
        # left space
        # right space
        # star
        # print line
        if j < i-1:
            print(" ", end=" ")
        elif j > lines:
            print(" ", end=" ")
        elif (i == 0 and j == 0) | (i == 0 and j == size-1):
            print(" ", end=" ")
        else:
            print("*", end=" ")

    lines -= 1
    print()
