"""
List Methods 
Use list methods to perform the following operations.
(Use List Methods Reference as guide)
Make sure to do the problems sections in order a --> d
"""

# 1) given the list, days, perform the following: 
days =  ['Mon', 'Tue', 'Wed', 'Fri', 'Sat']
# a) add the string 'Sun' to the end of the list 
print( days.append('Sun'))
print(days)
# b) add the string 'Thu' after 'Wed'
days.insert(3,"Thu")
print(days)
# c) reverse the order of this list ('Sun' ... 'Mon')
days.reverse()
print(days)
# d) display the list

# 2) given the list, months, perform the following: 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Mug', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Fog']
# a) remove the last element from the list
months.remove("Fog")
# b) remove the value 'Mug' from the list
months.remove("Mug")
print(months)
# c) what is the index position of the element 'Aug'?
print(months.index('Aug'))
print(months)
# d) display the list 

# 3) given the list, numbers, perform the following:
numbers = [1, 3, 4, 2, 5, 3, 7, 12, 9, 6, 8, 12, 10, 11]
# a) sort the list in ascending order (lowest number to highest number)
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)
# b) count how many number 5's are there on this list
fives= numbers.count((5))
print(fives)
# c) find the range of this list (range = highest number - lowest number) 
max= max(numbers)
min= min(numbers)
range = max-min
print(range)
    #HINT: method not required, do (a) first, then use indexing to get the range
# d) display the list 
