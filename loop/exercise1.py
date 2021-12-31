#Exercise 8: Generate a Python list of all the even numbers between 4 to 30
x= list(range(4,30))
def generate():
    for number in list(range(4,30)):
        if number%2==0:
          print(number)
        else:
           print("it is not even")
generate()