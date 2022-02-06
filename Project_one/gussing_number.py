

for guess in range(1,100):
    guess = int(input("guess a number between 1 to 100:   "))
    if guess == 100:
        print("that is right")
        break
    elif guess >100:
        print("please lower")
    elif guess<100:
        print("higher ")
        
    
    