# threading example 01

import threading
# uses single core
# maximises the use of single core by switching between threads
# not suitable for CPU bound tasks
# suitable for IO bound tasks
# e.g. network requests, file operations, database operations
# e.g. web scraping, web crawling, web requests, file reading, file writing, file copying, file downloading, file uploading, database reading, database writing, database updating, database deleting


def print_numbers():
    for i in range(1, 11):
        print(i)

def print_alphabets():
    for i in range(65, 75):
        print(chr(i))

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_alphabets)

t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")