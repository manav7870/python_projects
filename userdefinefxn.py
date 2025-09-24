# User-defined Functions

# def greet():
#     print("Hello World")

# def add():
#     x=int(input("Enter value of x: "))
#     y=int(input("Enter value of y: "))
#     print(f"Addition: {x+y}")

# def sum(a,b):
#     print(f"Addition: {a+b}")

# greet()
# add()
# greet()
# greet()
# sum(44,66)
# add()

#Task
# print("Report Card")

# def grades (a,b,c,d,e):
#     print(f"Hindi: {a}")
#     print(f"English: {b}")
#     print(f"Maths: {c}")
#     print(f"Science: {d}")
#     print(f"Punjabi: {e}")    
#     total=a+b+c+d+e    
#     print(f"Total Marks: {total}")
#     print(f"Average: {(total)/5}")

# grades(99,87,89,90,85)


# def multi(a,b):
#     return a*b

# print(f"Product: {multi(55,77)}")

#Task
def greet(a):
    i=1
    count=0
    for i in range(1,a+1):
        if a%i==0:
            count+=1
    return count

r=greet(4)
if r==2:
    print("Number is prime")
else:
    print("Number is composite")        
