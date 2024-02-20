class A:
    def sayhi(self):
        print("A")


class B:
    def sayhi(self):
        print("B")


class M(B, A):
    pass

new = M()
new.sayhi()
