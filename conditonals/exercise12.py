"""
Thrift Book Shop
You are operating a Thrift Book Shop where you sell books wholesale (multiple books with each transaction).
The prices of the wholesale books depend on the condition of the books: 
> New: $3.00 per book
> Good: $2.50 per book
> Fair: $1.50 per book
> Poor: $1.00 per book
Assume that the customer will only buy from one category (book condition) with each transaction. 
For example, customer A will only buy 12 New books (not 3 New, 4 Good, etc.)
Write a program that asks the user for the number of books they're purchasing and the condition of these 
books and calculate the final amount.
"""
number_of_books = int(input("how many books you are purchasing?  "))
condition = str(input(" what conditions of books you want to pusrchase? New, Good, Fair, Poor "))
if condition == "New":
    print(number_of_books*3.00)
    
elif condition == "Good":
    print(number_of_books*2.50)
elif condition == "Fair":
    print(number_of_books*1.50)
elif condition == "poor":
    print(number_of_books*1.00)