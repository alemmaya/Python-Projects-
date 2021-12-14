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

quote = "The Grass Hopper Lies Heavy"

#(1) Use String Methods to display the following Outputs:
#--OUTPUT: THE GRASS HOPPER LIES HEAVY
x = quote.upper()
print(x)
#--OUTPUT: the grass hopper lies heavy
print(quote.lower())
#--OUTPUT: The Grass Hopper Dies Heavy
print(quote.title())
#--OUTPUT: The Green Hopper Lies Heavy
print (quote.replace("Lies","Dies"))

#(2) How many 'e' letters are in the quote variable? 
e= quote.count('e')
print(e)

#(3) At what index does the word Heavy start? 
Heavy= quote.index('H')
print(Heavy)