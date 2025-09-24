my_list=["apple","mango","cherry","banana","watermelon","mango","gauva"]
# print(my_list)
# print(type(my_list))

# print(my_list[0])
# print(my_list[-1])

# print(my_list[2:6])
# print(my_list[2:])
# print(my_list[:6])

# print(len(my_list))

# marks=[44,66,77,99,44,23,77,44,66,43]
# print(marks.count(66))
# print(sum(marks))
# print(max(marks))
# print(min(marks))


# for item in my_list:
#     print(item)


# if "mango" in my_list:
#     print("Found")
# else:
#     print("Not Found")


# my_list.append("coconut")
# print(my_list)

# my_list.insert(4,"muskmelon")
# print(my_list)

a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     if i%2 == 0:
#         print(i)


my_list[2]="mango"
print(my_list)

my_list.remove("banana")
print(my_list)

my_list.pop(2)
print(my_list)

my_list.pop()
print(my_list)

# del my_list
# print(my_list)

# my_list.clear()
# print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

l1=["A","B","C"]
l2=["a","b","d"]
l3=l1+l2
print(l3)


l4=l3.copy()
print(l4)

#Task
while True:
    a=int(input("Enter the value of a: "))
    if a==1:
        x=input("Enter the append item: ")
        my_list.append(x)
        print(my_list)
    elif a==2:
        j=int(input("Enter the value of index no: "))
        y=input("Enter the item to insert: ")
        my_list.insert(j,y)
        print(my_list)
    elif a==3:
        z=input("Enter the item to be remove: ")
        my_list.remove(z)
        print(my_list)
    elif a==4:
        my_list.sort()
        print(my_list)
    elif a==5:
        i=input("Enter the value of index no: ")
        my_list.pop(i)
        print(my_list)
    elif a == 6: 
        print("Exiting...")
        break
    else:
        print("Invalid Choice")    
      

