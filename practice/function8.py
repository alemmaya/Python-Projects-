#Fuel cost calculator
#Write a function that takes a distance as a required argument, mpg (default 50 mpg) and fuel costs (default $1 a litre) as optional arguments. The function should return the cost in dollars.
def cost_cal(dis,fuel):
    cost= dis*fuel
    print(cost)
cost_cal(50,1)
cost_cal(20,3)

