# write python program for anagrams
input_list = ['tea', 'eat', 'tat', 'ata', 'tae', 'nat']
# expected out put
# output = [['tea','eat','tae'],['tat','ata'],['nat']]

anagram_list = []

for i in input_list:
    temp = []
    for j in input_list:
        if sorted(i) == sorted(j):
            temp.append(j)
    if temp not in anagram_list:
        anagram_list.append(temp)
print("Input list:", input_list)
print("Anagram List", anagram_list)
