"""--------------------Exercise 5----------------------------------------------------
Use String Concatenation and Slicing to answer the question below
--------------------------------------------------------------------------------"""

#(1) Use what you know about string concatenation and slicing to separate these words into their own categories
basket1 = 'Cat NY Red'
basket2 = 'MD Blue Bat'
basket3 = 'Green Rat VA'
basket4 = 'CA Yellow Owl'
print(basket1[0:3]+ " " + basket2[8:12]+ " " + basket3[6:10] + " " + basket4[10:13])
print(basket1[4:7]+ " " + basket2[0:3]+ " " + basket3[10:113] + " " + basket4[0:2])
print(basket1[7:11]+ " " + basket2[3:7]+ " " + basket3[0:5] + " " + basket4[3:9])

# So, display all animals in one line, all states in another line..etc. It might be helpful to store your slices in variables.
