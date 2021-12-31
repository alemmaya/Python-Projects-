import datetime
from datetime import date
#Days till Christmas
#Write a function that calculates how many days it is until Christmas and returns the number of days.
today  = date.today()
print(today)
christimas_day = date(2021,12,25)
print(christimas_day)
Days_till_christimas= abs((christimas_day-today).days)
print(Days_till_christimas)