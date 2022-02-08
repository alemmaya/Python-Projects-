import random
 
random_number = random.randint(1,100)

print(random_number) 
username = input("Hello, What's your Name?  ")
print("Hello", username+",", )
count=0
guess =0
while guess != random_number:
        guess = int(input("Guess a number between 1-100: "))
        count+=1
        
        if guess < random_number:
            if guess <0:
                print("Please keep your guess between 0 and 100")
            else:
                print("hmm.. Higher...")
        if guess > random_number:
            if guess >0:
                print("Please keep your guess between 0 and 100")
            print("hmm..lower")
print(f"your Guess count is {count}")
print("Bravo, correct answer!")
        
 