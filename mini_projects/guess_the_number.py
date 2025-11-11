# for creating guess numbere game we need a modulte "random" we heave to import it
import random   #random module for random numers

target = random.randint(1, 50)

while True: 
    userchoice = int(input("Guess the target value: "))
    if userchoice==target:
        print("Success: Correct guess!!")
        break
    elif userchoice>target:
        print("You Guessed greater value, plz enter smaller value: ")
    else:
        print("You Guessed smaller value, plz choose greater value: ")

print("-------GAME OVER-------")