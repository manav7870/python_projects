#Random Numbers
#Python program for generating random float number
import random
num=random.random()
print(num)

num=random.randint(1,500)
print( num )

#To generate value between specific range
num = random.randrange(1, 10)
print( num )
num= random.randrange(1, 10, 2)
print( num )

#To select a random element
import random
random_s = random.choice('Random Module') #a string
print(random_s)
random_1 = random.choice([23, 54, 765, 23, 45, 45]) #a list
print(random_1)
random_s = random.choice((12, 64, 23, 54, 34)) 
print(random_s)

#To shuffle elements in the list
list1 = [34,23,65,86,23,43]
random.shuffle( list1 )
print( list1 )
random.shuffle( list1 )
print(list1)