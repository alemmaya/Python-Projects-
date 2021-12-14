"""
String Interpolation 
"""

name = 'Andy'
hobby = 'Skiing'

# String Interpolation Output: My name is Andy and I like Skiing.
# f-string interpolation 
print(f'My name is {name} and I like {hobby}.')
# another way is to use the .format() method 
print('My name is {} and I like {}.'.format(name, hobby))

# Your Turn: 

# a) Create two variables, my_name and my_hobby, and write your name and your hobby.
my_name = "mimi"
my_hobby = "meeting new people"
# b) Using string interpolation, display the following output: My name is my_name and I like my_hobby.
print(f'My name is {my_name} and i like {my_hobby}.')
# c) Given the variables below, display the following output: The 3 books cost 12.99 each, and the total is 38.97 dollars.

books = 3
cost = 12.99
total = books*cost
print(f'The {books} cost {cost} each,and the total is {total} dollar' )