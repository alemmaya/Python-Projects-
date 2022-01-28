"""
A kitchen tile at lowe's has the following pricing structure:
1-10 tiles = $6.25 per tile
11-20 tiles = cost of 10 tiles + $5.50 for each additional tile
21-30 tiles = cost of 20 tiles + $4.75 for each additional tile
more than 30 tiles = cost of 20 tiles + $2.75 for each additional tile

- write a program that asks the user to enter the number of tiles they would 
like to purchase and calculate the cost.
- For customers who purchase more than 30 tiles, ask if they are a repeat costumer.
If so, offer a 10% discount off the total.
- display the total cost.
"""
number_of_tiles= int(input("please enter the number of tiles you would like to purchase:  "))
if  1 <number_of_tiles<10:
    cost_tiles = number_of_tiles*6.5
    print(cost_tiles)

elif 21<number_of_tiles <30:
     y= 65 + 4.75*(number_of_tiles-10)
     print(y)
elif number_of_tiles >30:
     y= 65 + 4.75*(number_of_tiles-20)
     print(y)