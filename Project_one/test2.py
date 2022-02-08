import random
 
random_number = random.randint(1,100)

print(random_number) 
username = input("Hello, What's your Name?  ")
print("Hello", username+",", )
count=0
guess =0
prompt = True

while prompt:
    user_input = int(input('guess a number between 1 and 100: '))
    if user_input == random_number:
        print('correct!')
        print(f"your Guess count is {count}")
        print("Bravo, correct answer!") 
        prompt = False
    else:
        print('try again!')
        count+=1
        continue