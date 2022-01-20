"""
- Ask the user: 'are you a returning customer? (Y/N)' 
if the user types Y, apply a 10% discount, then display the total due 
if the user types N, display the total due and this message: 'here is a coupon for next time.' 
- Display a thank you message at the end. 
"""

total = 326.45 

# Start here 
question = input('Are you a returning costumer? (Y/N)')

if question == 'Y':
    discount = total * 0.10
    total = total - discount 
    print('Your total: ', total)
elif question == 'N':
    print('Your total: ', total)
    print('here is a coupon for next time.')