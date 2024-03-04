"""
Student data: {John: 70, Kyle: 60, Steve: 50, Marsh: 40, Lucie: 50, Rama: 70, Krishna: 30, Mahesh: 40, Suresh: 40, Naresh: 60}

Input: Rank = 1
Output: John, Rama 	- find the first highest scored candidate names

Input: Rank = 2
Output: Kyle, Naresh  	- find the second highest scored candidate names

Input: Rank = 3
Output: Steve, Lucie  	- find the third highest scored candidate names


"""
student_marks = {'John': 70, 'Kyle': 60, 'Steve': 50, 'Marsh': 40, 'Lucie': 50, 'Rama': 70, 'Krishna': 30, 'Mahesh': 40, 'Suresh': 40, 'Naresh': 60}

# find the first highest scored candidate names
rank = 3
sorted_marks = sorted(student_marks.items(), key=lambda x: x[1], reverse=True)
print(sorted_marks)
print("Input: Rank =", rank)
print("Output:", end=" ")
for i in range(rank):
    print("Rank {}: Name: {} Marks:{}".format(i+1, sorted_marks[i][0], sorted_marks[i][1]))
    # print(sorted_marks[i][0], end=", ")
print("\t- find the first highest scored candidate names")
