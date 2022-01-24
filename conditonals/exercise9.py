"""
Thrift Book Shop
You are operating a Thrift Book Shop where you sell books wholesale (multiple books with each transaction).
The prices of the wholesale books depend on the condition of the books: 
> New: 
    - Customer buying 1 - 5 books: $3.00 per book
    - Customer buying more than 5 books: $2.75 per book
> Fair: 
    - Customer buying 1 - 5 books: $2.00 per book
    - Customer buying more than 5 books: $1.75 per book
> Poor: 
    - Customer buying 1 - 5 books: $1.00 per book
    - Customer buying more than 5 books: $0.75 per book
    
Assume that the customer will only buy from one category (book condition) with each transaction. 
For example, customer A will only buy 12 New books (not 3 New, 4 Good, etc.)
Write a program that asks the user for the number of books they're purchasing and the condition of these 
books and calculate the final amount.
"""
condition = str(input("what condtion of book you are purchasing? New,Fair,Poor"))
number_of_books =int(input("How many books you want to purchase?")) 
if  condition == "New":
    if 1<number_of_books<5:
        print(number_of_books*3)
    elif number_of_books>5: 
        print(number_of_books*2.75)
elif condition== "Fair":
    if 1<number_of_books<5:
        print(number_of_books*2)
    elif number_of_books>5: 
        print(number_of_books*1.75)
elif condition == "Poor":
    if 1<number_of_books<5:
        print(number_of_books*1)
    elif number_of_books>5: 
        print(number_of_books*0.75)