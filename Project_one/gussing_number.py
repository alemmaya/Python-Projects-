
# Welcome to the world Number one guessing game 
guess=100
for guess in range(1,100):
    guess = int(input("guess a number between 1 to 100:   "))
    if guess == 100:
        print("that is right")
        break
    elif guess >100:
        print("your guess is too high")
    elif guess<100:
        print("your guess is too low")
        
    
    