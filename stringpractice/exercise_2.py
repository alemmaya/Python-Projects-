"""
String indexing and concatenation

given the variable 'letters' below, using ONLY string indexing and concatenation, create the variables and produce the desired output. 
You should create the values by indexing the variable 'letters' below and concatenating (adding) the letters to form the desired output. 

Index counting will be a bit tedious so to make things easier, you may refer to the key below. It will help you count and find indexes faster:
letters[0]  ---> a 
letters[5] ---> f
letters[10] ---> k
letters[15] ---> p
letters[20] ---> u
letters[25] ---> z
"""

letters = "abcdefghijklmnopqrstuvwxyz"

# Example: create variable a, with string value 'bat'
a = letters[1] + letters[0] + letters[19]
print(a)  # Output: bat 

# Example: create variable b, with string value 'gold'
b = letters[6] + letters[14] + letters[11] + letters[3]
print(b)  # Output: gold


# ---- Your Turn ----- 
# create varaible c, with string value 'cold'
c= letters[2] + letters[14] + letters[11] +letters[3]
print(c)
# create variable d, with string value 'dog'
d= letters[3] + letters[14] + letters[6]
print(d)
# create variable e, with string value 'back'
e= letters[2] + letters[14] + letters[11] +letters[3]
# create variable f, with string value 'aught'
f= letters[0] + letters[20] + letters[6] +letters[7] + letters[19]
print(f)