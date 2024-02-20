class Demo:
    count = 0
    def __init__(self):
        Demo.count += 1  # increment count by 1 in constructor class variable

    def getcount(self):
        print(Demo.count)


d1 = Demo()
d2 = Demo()
d3 = Demo()

d1.getcount()
d2.getcount()
d3.getcount()