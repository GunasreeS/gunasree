class A:
    def robot():
        print("In class A robot Method")
class B(A):
    def car():
        print("In class B car Method")
class C(B):
    def name():
        print("In class C name Method")

class D:
    def robot():
        print("In class D monitor Method")
class E(D):
    def car():
        print("In class B car Method")
class F(E):
    def name():
        print("In class C name Method")
