"""
- Ask the user: 'what day is it today?' and display a number that represent that day of the week.
    For example, if the user's input is 'Tuesday', the output would be 2. 
    If the user's input is 'Friday', output is 5, etc.
- If the user's input is not a day of the week, display the message:
    'invalid input! But today is the perfect day to learn something new.'
- Assume the user will type the days in capital case (Monday, Tuesday, Wednesday), but for extra points, you 
can turn all input into lowercase before running the conditional statement. if you use the .lower() method, make sure 
the stay consistent throughout the conditional statements. 
"""

day = input('what day is it today?').lower()

if day == 'monday':
    print(1)
elif day == 'tuesday':
    print(2)
elif day == 'wednesday':
    print(3)
elif day == 'thursday':
    print(4)
elif day == 'friday':
    print(5)
elif day == 'saturday':
    print(6)
elif day == 'sunday':
    print(7)
else:
    print('invalid input! But today is the perfect day to learn something new.')