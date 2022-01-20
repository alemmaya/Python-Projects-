"""
- Ask the user for a number that represents the month they were born, for instance, 7 for July or 12 for December.
- Based on the user's input, do the following: 
if number equals 12, or 1, or 2, display the message: 'Winter is not a season, it is a celebration.'
if number is between 3 and 5, display the message: 'Spring unlocks the flowers to paint the laughing soil.'
if number is between 6 and 8, display the message: 'In summer, the song sings itself.'
if number is between 9 and 11, display the message: 'Fall shows us how beautiful it is to let things go.'
if user's input is not in any of the choices above, display the message: 'Invalid input! It is tax season somewhere.'
"""

list_months = """
    1. January
    2. Feburary
    3. March
    4. April
    5. May
    6. June
    7. July
    8. August
    9. September
    10.October
    11.November
    12.December
"""
print(list_months)
x= int(input("Type a number that represents the month they were born:   "))
if (x== 12) or (x==1) or(x==2):
    print('Winter is not a season, it is a celebration.')
elif 3<x<5:
    print('Spring unlocks the flowers to paint the laughing soil.')
elif 6<x<8:
    print('In summer, the song sings itself.')
elif 9<x<11:
    print('Fall shows us how beautiful it is to let things go.')
else:
    print('Invalid input! It is tax season somewhere.')
