"""
- Ask the user to look at the menu and select a number that represents today 
- if today is Saturday or Sunday, display the message: 'Have a good weekend!'
- if today is any other day of the week, display the message: 'Enjoy the week!' 
"""

menu = """
1. Monday
2. Tuesday
3. Wednesday
4. Thursday
5. Friday 
6. Saturday
7. Sunday 
"""
print(menu)

# Start here 
day = int(input('Look at the menu and select a number that represents today:'))

if day == 6 or day == 7:
    print('Have a good weekend!')
elif 1 <= day <= 5:
    print('Enjoy the week!')

# Hmmmm.... what if the user's input is not a value between 1 and 7 (say 100), what would be the output?


