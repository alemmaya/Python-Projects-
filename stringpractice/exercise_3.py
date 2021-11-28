"""
String slicing

using the quote below, create variables and produce the desired output by slicing the words from the quote.
"""

malcolm = "Education is the passport to the future, for tomorrow belongs to those who prepare for it today."


# Example: create variable a, with string value 'future'
a = malcolm[33:39]  
#print(a)  # Output: future

# ----- Your Turn ----- 
# create variable b, with string value 'Education'
b= malcolm.find('Education')
print(b)
#(0,8)
# create variable c, with string value 'passport'
c= malcolm.find('passport')
print(c)
#(17,25)
# create variable d, with string value 'tomorrow'
d= malcolm.find('tomorrow')
print(d)
#(45,53)
# create variable e, with string value 'passport to the future'
e= malcolm.find('passport to the future')
print(e)
#(17,39)
# create variable f, with string value 'tomorrow belongs to those who prepare for it today.'
f= malcolm.find('tomorrow belongs to those who prepare for it today')
print(f)
#(45,95)