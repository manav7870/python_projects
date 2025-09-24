# class A:
#     def displayA(self):
#         print("Hello World")
# a1=A()
# a1.displayA()

# class B:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

# #     def __str__(self):
# #         return f"{self.name} {self.marks}"

#     def displayB(self):
#         print(f"Name: {self.name}")    
#         print(f"Marks: {self.marks}")    

# # b1=B("Rahul",98)
# b1.displayB()
# print(b1)        

# # Inheritance
# # 1)Single Inheritance
# class A:
#     def displayA(self):
#         print("Parent Class")

# class B(A):
#     def displayB(self):
#         print("Child Class")

# b1=B()
# b1.displayA()
# b1.displayB()

# # 2)Multilevel Inheritance
# class A:
#     def displayA(self):
#         print("A Class")

# class B(A):
#     def displayB(self):
#         print("B Class")

# class C(B):
#     def displayC(self):
#         print("C Class")


# c1=C()
# c1.displayA()
# c1.displayB()
# c1.displayC()


# # 3)Multiple Inheritance
# class A:
#     def displayA(self):
#         print("A Class")

# class B:
#     def displayB(self):
#         print("B Class")

# class C(A,B):
#     def displayC(self):
#         print("C Class")


# c1=C()
# c1.displayA()
# c1.displayB()
# c1.displayC()

# #Task
# class A:
#     def displayA(self,num):
#         self.num=num

# class B(A):
#     def displayB(self):
#         for i in range(1,11):
#             print(f"{self.num} X {i} = {self.num*i}")

# b1=B()
# b1.displayA(67)
# b1.displayB()

# #Task
# class A:
#     def displayA(self,a):
#         self.a=a
# class B:
#     def displayB(self,b):
#         self.b=b 
# class C(A,B):
#     def displayC(self):
#         print(f"Addition: {self.a+self.b}")

# c1=C()
# c1.displayA(1)              
# c1.displayB(2)              
# c1.displayC()  


# #Task //Multiple Inheritance
# class A:
#     def displayA(self,x):
#         self.x=x
# class B:
#     def displayB(self,y):
#         self.y=y
# class C(A,B):
#     def displayC(self):
#         print(f"Addition: {self.x+self.y}")

# c1=C()
# x=int(input("Enter the value of x: "))
# c1.displayA(x)              
# y=int(input("Enter the value of y: "))
# c1.displayB(y)              
# c1.displayC()    


# #Task //Multilevel Inheritance
# class A:
#     def displayA(self,x):
#         self.x=x
# class B(A):
#     def displayB(self,y):
#         self.y=y
# class C(B):
#     def displayC(self):
#         print(f"Addition: {self.x+self.y}")

# c1=C()
# x=int(input("Enter the value of x: "))
# c1.displayA(x)              
# y=int(input("Enter the value of y: "))
# c1.displayB(y)              
# c1.displayC()              

# #Task
# class A:
#     def displayA(self,a,b,c,d,e):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         self.e=e
# class B(A):
#     def displayB(self):
#         self.total=self.a+self.b+self.c+self.d+self.e
#         print(f"Total marks: {self.total}")
# class C(B):
#     def displayC(self):
#         avg=self.total/5
#         print(f"Average: {avg}")
# c1=C()
# a=int(input("Enter the value of a: "))
# b=int(input("Enter the value of b: "))
# c=int(input("Enter the value of c: "))
# d=int(input("Enter the value of d: "))
# e=int(input("Enter the value of e: "))
# c1.displayA(a,b,c,d,e)                               
# c1.displayB()                
# c1.displayC()                
                

# # 4)Hierarchical Inheritance

# class A:
#     def displayA(self):
#         print("Class A")

# class B(A):
#     def displayB(self):
#         print("Class B")

# class C(A):
#     def displayC(self):
#         print("Class C")


# b1=B()
# b1.displayA()
# b1.displayB()

# c1=C()
# c1.displayA()
# c1.displayC()

#Method Overriding
class A:
    def display(self):
        print("Parent Class")

class B(A):
    def display(self):
        super().display()
        print("Child Class")

b1=B()
b1.display()                