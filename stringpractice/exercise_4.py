"""
String slicing and concatenation

using string slicing and concatenation, produce the following outputs:
"""

fruits = "apple banana avocado"
veggies = "potatoe carrot lemon"
protein = "chicken eggs beef"
bakery = "bread bagel toast"
fridge = "juice smoothie ice cream"



# Example: create variable a, with string value 'banana smoothie'
a = fruits[6:13] + fridge[6:14]
print(a)  # Output: banana smoothie

# ---- Your Turn -----

# create variable b, with string value 'avocado toast'
b= fruits[13:20] + bakery[11:17]
print(b)
# create variable c, with string value 'lemon juice'
c= veggies[15:20] + fridge[0:5]
print(c)
# create variable d, with string value 'potato ice cream'
d= veggies[0:7] + fridge[14:24]
print(d)
# create variable e, with string value 'bagel with eggs'. Use the variable 'extra' below
extra = 'with'
e= bakery[6:12]+extra[0:4] +protein[7:13]
print(e)
# create variable f, with string value 'chicken and cheese burrito'. Use the variable 'more' below
more = 'cheese and burrito'
# comment on cheese with burrito 
f= protein[0:8] + more[0:18]
print(f)