import random
num=random.randint(1,10)

chances=5
while chances>0:
    guess=int(input("Enter Guess: "))
    if guess== num:
        print("You Won")
        break
    else:
        print("You guessed wrong try again")
    chances=chances-1
if chances==0:
    print("You LOST")