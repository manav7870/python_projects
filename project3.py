#Number Guessing Game

import random
num = random.randint(1, 100)
attempts = 0
Max_attempts = 7
print("Number Guesssing Game")
print("Lets Begin!!")
while True:
    try:
        a = int(input("Guess the number between (1-100): "))
        attempts+=1
        if a == num:
            print(f"Hurray!!You guessed a right number in {attempts} attempts!!")
        elif a < num:
            print("Too small!! Try something Big.." )
        elif a > num:
            print("Too Big!! Try something small..")   
        else:
            print("Enter a number between (1-100) !!")    
            break
    except ValueError:
        if attempts == Max_attempts and a != num:
            print(f"You have reached maximum attempts!! The number is {num}") 
        
    
    
