# reverse number

def reverse_number(num):
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = (reverse_num * 10) + remainder
        num = num // 10
    return reverse_num

print(reverse_number(1234))