import random

num=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Enter the number between 1-100: "))
    attempts+=1
    if guess<num:
        print("Too less! Try again!")
    elif guess>num:
        print("Too Big! Try Again!")
    else:
        print(f"Correct! You guessed in {attempts} attempts")        
        break
