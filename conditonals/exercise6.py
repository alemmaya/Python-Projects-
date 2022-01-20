"""
- Ask the user to type an integer, n between 1 and 10 (1 <= n <= 10), then perform an operation based on the following:
- number n is between 1 and 3 inclusive (that is, 1<= n <= 3):
    > output: 3*n
- number n is between 4 and 6 inclusive:
    > output: 5*n
- number n is between 7 and 10 inclusive:
    > output: 8.5*n 
- if the user's given number is any number other than 1 <= n <= 10:
    > display the message: invalid input.

"""
n = int(input('Type a number between 1 and 10: '))

if 1 <= n <= 3:
    print(2*n)
elif 4 <= n <= 6:
    print(5*n)
elif 7 <= n <= 10:
    print(8.5*n)
else:
    print('invalid input.')
    

