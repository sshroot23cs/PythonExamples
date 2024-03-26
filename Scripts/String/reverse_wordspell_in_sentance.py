string = "Try programiz.pro here"
# output: yrT .zimargorp.orp ereh
word_list = string.split(" ")

def reverse_word(given_string):
    reversed_string = ""
    for char in given_string:
        reversed_string = char + reversed_string
    return reversed_string

print(" ".join(map(reverse_word, word_list)))
# print(" ".join(map(lambda x: x[::-1], word_list)))
# print(" ".join([x[::-1] for x in word_list]))