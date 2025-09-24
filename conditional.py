# Conditional Statements
# 1)if statement
# num=67
# if num < 70:
#     print("Smaller")
# else:
#     print("Greater")

# x=10
# if x%2==0:
#     print("It is even number")
# else:
#     print("It is odd number")

# a=1
# b=2
# if a == b:
#     print("a and b are equal")
# else:
#     print("a and b are not equal")

# if a != b:
#     print("They are not equal")
# else:
#     print("They are equal")
# if a<0:
#     print("It is negative")
# else:
#     print("It is positive")    

# IF,ELSE,ELIF
# print("Report Card")
# a= int(input("Hindi: "))                        
# b= int(input("English: "))                        
# c= int(input("Punjabi: "))                        
# d= int(input("Science: "))                        
# e= int(input("Maths: "))                        
# total=a+b+c+d+e
# print(f"Total Marks: {total}")
# avg= total/5
# if avg > 90:
#     print("Grade is A")
# elif avg >80:
#     print("Grade is B")
# elif avg > 70:
#     print("Grade is C")
# else:
#     print("You are fail")    


# num=int(input("Enter any number: "))
# print(num)
# print(type(num))

# Nested IF-ELSE
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
if a>b:
    if a>c:
        print("A is Greatest")
    else:
        print("C is Greatest")
else:
    if b>c:
        print("B is Greatest")
    else:
        print("C is Greatest")                