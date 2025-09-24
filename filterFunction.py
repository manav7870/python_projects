# Filter Function
my_list=[56,88,54,34,32,33,66,55,89,7,6,21]

def is_even(number):
    return number%2 == 0

el=list(filter(is_even,my_list))
print(el)


# Lambda Function
x= lambda a: a+10
print(x(5))

x= lambda a,b: a+b
print(x(54,78))

x= lambda a,b,c: a+b+c
print(x(55,78,87))


my_list=[56,88,54,34,32,33,66,55,89,7,6,21]
el=list(filter(lambda number: number%2 == 0 and number > 50,my_list))
print(el)
