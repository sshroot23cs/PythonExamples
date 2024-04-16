# print even number till n

n = 10
even_numbers = [i for i in range(1, n) if i % 2 == 0]
print(even_numbers)


# generator
def generate_even_no(num_list):
    for i in range(1, num_list):
        if i % 3 == 0:
            yield i
            yield i * i
        if i % 5 == 0:
            yield i
            yield i * 10
        yield ("Sushrut"
               "")


num_list = 10
even_num_list = generate_even_no(num_list)
for n in generate_even_no(num_list):
    print(n)

