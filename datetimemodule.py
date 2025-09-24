import datetime
x= datetime.datetime.now()
print(x)

#Return the year and name of weakday:
print(x.year)
print(x.strftime("%a"))
print(x.strftime("%A"))

print(x.strftime("%b"))
print(x.strftime("%B"))

print(x.strftime("%y"))
print(x.strftime("%Y"))

print(x.strftime(" %H "))
print(x.strftime(" %I "))
print(x.strftime(" %p "))
print(x.strftime(" %M "))
print(x.strftime(" %S "))


