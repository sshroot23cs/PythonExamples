class Demo:
    count = 0

    def __init__(self):
        self.count = 0  # instance variable
        Demo.count += 1  # increment count by 1 in constructor class variable

    @classmethod
    def get_class_count(cls):
        print(cls.count)


d1 = Demo()
d2 = Demo()
d3 = Demo()

d1.get_class_count()  # 3
d2.get_class_count()  # 3
d3.get_class_count()  # 3
