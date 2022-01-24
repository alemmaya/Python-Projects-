"""
Write a program that asks the user for the temperature and returns a message that corresponds to the following input: 
(Consider values given by the user that are not in the range. Assume temperature does not go below -10 or above 120)

Temperature is less than 30
Message: It is too cold to go outside.
Temperature is between 30 and 45
Message: It is cold. Wear a jacket.
Temperature is between 46 and 75
Message: The temperature is decent. Is it raining?
Temperature is between 76 and 85
Message: The weather is perfect!
Temperature is more than 86
Message: It is hot outside. Stay hydrated!

"""
Temperature = int(input("What is the temprature?   "))
if Temperature < 30:
    print("It is too cold to go outside")
elif  30 <Temperature< 45:
    print("It is cold. Wear a jacket.")
elif  46<Temperature<75:
    print("The temperature is decent. Is it raining?")
elif  76<Temperature < 85:
    print("The weather is perfect!")
elif Temperature >86:
    print("It is hot outside. Stay hydrated!")
