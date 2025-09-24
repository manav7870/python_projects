my_set={"apple","banana","banana","mango",True,1,"cherry","coconut","plum",0,False,"mango"}
print(my_set)
print(type(my_set))

for item in my_set:
    print(item)

if "mango" in my_set:
    print("Found")
else:
    print("Not found")


my_set.add("gauva")
print(my_set)


# my_set.clear()
# print(my_set)
x=my_set.pop()
print(x)

my_set.remove("cherry")
print(my_set)

t1={"A","B","C"}
t2={"a","b","c"}
t1.update(t2)
print(t1)

# task
a={1,2,3,4,5,6,7,8,9,10}
# print(a)
# while True:
#     b=int(input("Enter the value of b: "))
#     if b==1:
#         c=input("Enter the item to add: ")
#         a.add(c)
#         print(a)
#     elif b==2:
#         d=int(input("Enter the item to be remove: "))
#         a.remove(d)
#         print(a)
#         break
#     else:
#         print("Invalid Choice")    
for item in a:
    print(item)

# my_set.remove("apple2")
# print(my_set)

# my_set.discard("apple")
# print(my_set)

# del my_set
# print(my_set)


