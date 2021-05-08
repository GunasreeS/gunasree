class A:
    #print("this is from parent class A")
    a=20
    
class B:
    #print("this is child class B")
    b=10
class C(A,B):
    print("this is class C")
ob=C
print(ob.a)
print(ob.b)
