my_tuple=("apple","mango","cherry","plum","coconut")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

a,b,c,d,e=my_tuple
print(a)
print(b)
print(c)
print(d)
print(e)

print(my_tuple[1:4])
print(my_tuple[1:])
print(my_tuple[:4])


for item in my_tuple:
    print(item)


if "mango" in my_tuple:
    print("found")
else:
    print("Not found")

print(len(my_tuple))

mt=(66,88,44,33,55,66,44,66,44,33)
print(mt.count(66))
print(sum(mt))
print(max(mt))
print(min(mt))

t1=("A","B","C")
t2=("a","b","c")
t3=t1+t2
print(t3)