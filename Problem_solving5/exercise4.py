"""
Math with Lists

Exam Scores: [79, 88, 75, 78, 89, 92, 80, 74, 90, 84, 63, 77, 81, 85, 97, 86, 76]

The numbers above represent exam scores of a class.
The exam is scored 0-100, where 0 is the lowest score possible, and 100 is the highest.

Using the functions and list methods, find the values below. 

Helpful functions:
len()   # returns length of the list
len()
sum()   # returns the sum of all elements in a list 
min()   # returns the lowest value in a list
max()   # returns the highest value in a list 
"""
scores = [79, 88, 75, 78, 89, 92, 80, 74, 90, 84, 63, 77, 81, 85, 97, 86, 76]

# 1) What was the average score of the whole class? 
max= max(scores)
print(max)
min=min(scores)
print(min)
average= max-min
print(average)

# 2) What was the highest score?
print(max)
# 3) What was the lowest score? 
print(min)
# 4) How many students scored a perfect score of 100? 
perfect_score =scores.count(100)
print( perfect_score)
# 5) Create a new list with all scores sorted in ascending order (low to high)
scores.sort()
print(scores)
# 6) If a score of 65 and higher is required to pass. How many students did not pass the exam?
k=65
count = len([i for i in scores if i > k])
print(count)