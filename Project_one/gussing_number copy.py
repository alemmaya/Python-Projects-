
# Welcome to the world Number one guessing game 
import random
answer= random.randint(0,100)
print(answer)
user_name = str(input("What is your name?:  "))      
while True:
    guess = int(input("guess a number between 1 to 100:   "))
    if guess !=answer:
        print("please try again")
        Incorrect_answer = []
        Incorrect_answer.append(guess)
        print(Incorrect_answer)
        
    if guess==answer:
        print("yay! you won!")
        print(Incorrect_answer)
        break
