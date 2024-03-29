class student:

    def __init__(self, name, age, std, grade):
        self.name = name
        self.age = age
        self.std = std
        self.grade = grade

    def print_student(self):
        print(self.name, self.age, self.std, self.grade)


a = student('std_a', 12, 5, 'A+')
b = student('std_b', 15, 6, 'A+')
c = student('std_c', 14, 7, 'A+')
d = student('std_d', 19, 8, 'A+')
e = student('std_e', 16, 9, 'A+')

std_ls = [a, c, b, d, e]
print("Unsorted list")
for obj in std_ls:
    obj.print_student()

# Sort the list of objects by age property using lambda function in sort method
std_ls.sort(key=lambda x: x.age)

print("Sorted list")
for obj in std_ls:
    obj.print_student()

# Sort the list of objects by age property without sort method
std_ls = [a, c, b, d, e]
for i in range(len(std_ls)):
    for j in range(i+1, len(std_ls)):
        if std_ls[i].age > std_ls[j].age:
            std_ls[i], std_ls[j] = std_ls[j], std_ls[i]
print("Sorted list without sort method")
for obj in std_ls:
    obj.print_student()
