# checking anagram
def is_anagram_using_sorted(str1, str2):
    return sorted(str1) == sorted(str2)

# using join() + sorted()
# checking anagram
def is_anagram_using_join(str1, str2):
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        return True
    return False

# write optimized code for anagram
str1 = "listen"
str2 = "silent"
def is_anagram_optimized(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in str1:
        if i in str2:
            str2 = str2.replace(i, '', 1)
    if str2 == '':
        return True
    return False

# calculate memory usage and time taken for anagram check of above 3 functions
import time
import os

def memory_usage_psutil():
    # return the memory usage in MB
    import psutil
    process = psutil.Process(os.getpid())
    mem = process.memory_info().rss / float(2 ** 20)
    return mem

def check_anagram():
    str1 = "listen"
    str2 = "silent"
    start_time = time.time()
    print(is_anagram_using_sorted(str1, str2))
    print("Time taken using sorted: ", time.time() - start_time)
    print("Memory used using sorted: ", memory_usage_psutil())

    start_time = time.time()
    print(is_anagram_using_join(str1, str2))
    print("Time taken using join: ", time.time() - start_time)
    print("Memory used using join: ", memory_usage_psutil())

    start_time = time.time()
    print(is_anagram_optimized(str1, str2))
    print("Time taken using optimized: ", time.time() - start_time)
    print("Memory used using optimized: ", memory_usage_psutil())


if __name__ == "__main__":

    check_anagram()

