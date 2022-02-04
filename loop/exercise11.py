"""
Study the example given below, then answer the exercise 
"""

# 6) Example: Ask the user to input the word 'Yes', keep asking until the correct value is given
while True:
    answer = input('please type Yes to continue: ')
    if answer == 'Yes':
        break
    else:
        print('Invalid input.')

print('done. Thank you')


# Run this code, see the output, then answer exercise 6


# 6) Exercise:  Use the input function with the following prompt: 'press 1 to continue'.
'''
Use a while loop, keep asking until the correct value is given 
if user presses 1, display the message 'operation continue!' and exit the loop
'''