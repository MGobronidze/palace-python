class A:
    def action(self):
        print("Action from A")

class B(A):
    def action(self):
        print("Action from B")
        super().action()

class C(A):
    def action(self):
        print("Action from C")
        super().action()

class D(B, C):
    def action(self):
        print("Action from D")
        super().action()

class E(D):
    def action(self):
        print("Action from E")
        super().action()

e = E()
e.action()

print(E.mro())  # ვნახოთ MRO-ის რიგი
