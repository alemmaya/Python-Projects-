"""-----------------------------------------------------
Use String Methods to answer the questions below
---Method---|----It's purpose----
.upper()    | change all into capital letters
.lower()    | change all into small letters
.split()    | split the string into separate words or to a chosen parameter
.replace()  | replace a chosen value
.index()    | search for the index of a specific value
.count()    | Count the occurence of a value
.format()   | string interpolation
.strip()    | remove spaces at the beginning and end of a string
-----------------------------------------------------------"""

# Given the methods above, choose an appropriate method to get the following ouputs:

a = 'To Infinity and Beyond'

# a) Output: TO INFINITY AND BEYOND
print(a.upper())
print(a.replace('i','X'))
# b) Output: to infinity and beyond 
print(a.lower())


# c) Output: To Xfinity and Beyond 
position = 3
new_character = 'X'

a= a[:position] + new_character +a[position+1:]
print(a)

b = 'The greatest glory in living lies not in never falling, but in rising every time we fall.'

# d) Output: the number of 'i' characters in variable b 
print(len('i'))

# e) Output: the index position of the word never
print(b.index('n'))

# f) Output: The greatest happiness in living. (hint: use slicing and a method)
new_string= b[0:28]
print(new_string)
print(new_string.replace("glory","happiness"))


# g) Use your imagination to use 3 different methods you haven't used before. Use variables above or create new variables

x = new_string.startswith("living")
print(x)

x = new_string.rfind("living")

print(x)
