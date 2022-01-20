"""
- Ask the user for today's temperature, then display a message based on the following:
the temperature is lower than 30:
    display the message 'stay inside and drink coffee'
temperature is between 30 and 44:
    display the message 'wear a sweater and go outside'
temperature is between 45 and 85:
    display the message 'go outside and play'
temperature is higher than 85:
    display the message 'stay inside and drink iced tea'
"""
# (1) Start here 
temp = int(input('temperature for today?'))

if temp < 30:
    print('stay inside and drink coffee')
elif 30 <= temp <= 44:
    print('wear a sweater and go outside')
elif 45 <= temp <= 85:
    print('go outside and play')
elif temp > 85:
    print('stay inside and drink iced tea')



# (2) Are there any design flaws on this program? If so, sxplain how would you solve them.

"""
Upper bound and lower bounds 
user can enter large values like 1000, or negative values like -1000
"""