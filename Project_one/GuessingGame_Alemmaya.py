
#Welcome to the number One Guessing Game
from importlib.machinery import all_suffixes
import random
 # generating random number 
random_number = random.randint(1,100)
# printing random number 
print(random_number) 
username = input("Hello, What's your Name?  ")
print("Hello", username+",", )
count=0
guess=0
prompt = True
# creating a container for holding the guessed number 
list =[]
# setting the conditons  the loop should iterate /terminate 
while prompt:
    user_input = int(input('guess a number between 1 and 100: '))
    if user_input != random_number:
        if user_input >100:
            print("Please only between 1 and 100")
        elif user_input <0:
            print("Please less than 100")
        elif user_input > random_number:
            print("hmm..lower")
            list.append(user_input) 
        elif user_input< random_number:
            print("hmm..higher")
            list.append(user_input)
        count+=1 
          
        prompt = True
        continue
    else:
        print('you are correct!')
        count+=1
        print(f"your guess count is {count}",list)
        break