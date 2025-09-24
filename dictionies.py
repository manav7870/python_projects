my_dict={
    'name':'rahul',
    'marks': 89,
    'age': 26,
    'city':'Mumbai',
    'emailid':'rahul@gmail.com'
}
print(my_dict)
print(type(my_dict))

print(my_dict['city'])

my_dict['grades']='B'
print(my_dict)

my_dict['city']="Khanna"
print(my_dict)

print(len(my_dict))

print(my_dict.get('emailid'))

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(f"{key} = {value}")

# my_dict.clear()
# print(my_dict)
print(my_dict)

my_dict.popitem()
print(my_dict)


a=my_dict.pop('city')
print(a)



# del my_dict
# print(my_dict)

#Task
a={
    'name': 'Manav',
    'age': '18',
    'city': 'Samrala',
    'marks': '89'
}
while True:
    b=int(input("Enter the value of b: "))
    if b==1:
        c=input("Enter the value you want to add: ")
        a['email']= (c)
        print(a)
    elif b==2:
        d=input("Enter the key to remove: ")
        a.pop(d)
        print(a)    
    elif b==3:
        e=input("Enter the key to change: ")
        f=input("Enter the value to change: ")
        a[e]=(f)
        print(a)
    else:
        print("Exiting...")
        break