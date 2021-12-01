"""--------------------Exercise 5----------------------------------------------------
Use String Concatenation and Slicing to answer the question below
--------------------------------------------------------------------------------"""

"""-----------------Extra Credit 1-----------------------
Use the tools you've learned to display the given output
--------------------------------------------------------"""

# Grab the words you need from the variables below. This one is tricky so be patient. 
basket1 = 'yesterday today tomorrow'
basket2 = 'important thing'
basket3 = 'Learn live hope stop question'
basket4 = 'from for is The to not'
basket5 = ' , . .. '

#DISPLAY THIS OUTPUT: Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning.
print(basket3[0:5] +" " + basket4[0:4]+ " "+ basket1[0:9] + "," + basket3[6:10]+" "+ basket4[5:7])
