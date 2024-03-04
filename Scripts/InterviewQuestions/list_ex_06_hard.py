# Input : s = “geeks for geeks contribute practice”, w1 = “geeks”, w2 = “practice”
# Output : 1
# There is only one word between the closest occurrences of w1 and w2.
#
# Input : s = “the quick the brown quick brown the frog”, w1 = “quick”, w2 = “frog”
# Output : 2


def find_closest_occurrences(s, w1, w2):
    words = s.split()
    w1_index = -1
    w2_index = -1
    min_distance = len(words)
    for i in range(len(words)):
        if words[i] == w1:
            w1_index = i
        if words[i] == w2:
            w2_index = i
        if w1_index != -1 and w2_index != -1:
            min_distance = min(min_distance, abs(w1_index - w2_index))
    return min_distance - 1


# s = "geeks for geeks contribute practice"
# w1 = "geeks"
# w2 = "practice"
# print(find_closest_occurrences(s, w1, w2))
# s = "the quick the brown quick brown the frog"
# w1 = "quick"
# w2 = "frog"
# print(find_closest_occurrences(s, w1, w2))

s = "apple mango banana apple grape dragon orange"
w1 = "apple"
w2 = "orange"
print(find_closest_occurrences(s, w1, w2))
