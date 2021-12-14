"""
List Indexing
"""

# 1) Given the list below, what is the output of the following? 
days =  ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# days[0]   #OUTPUT:Mon
print(days[0])
# days[-1]  #OUTPUT: Sun
print(days[-1])
# days[5]   #OUTPUT:Sat 
print(days[5])
# days[2]   #OUTPUT: Wed
print(days[2])
# 2) Given the list below, use indexing to produce the outputs below 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# OUTPUT: Jan 
print(months[0])
# OUTPUT: Dec
print(months[11])
# OUTPUT: Nov
print(months[10])
# OUTPUT: Jun
print(months[5])
# OUTPUT: May
print(months[4])

# 3) Given the string months_s and list months_l below, name advantages of indexing lists vs indexing strings
months_s = 'Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec'
#indexing string perhaps is specific enough to deal with each character 

months_l = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#indexing lists removes the manual counting for postions. we can use elements instead 