import pandas as pd
print(pd.__version__)
import os
os.getcwd()
x= os.getcwd()
print(x)
y= os.listdir()
print(y)
df_exams= pd.read_csv('StudentsPerformance.csv')
print(df_exams)
# show first five rows of the excel sheet
first_five = df_exams.head()
print(first_five)
# show the last five rows in the  source data 
last_five= df_exams.tail()
print(last_five)
# show the last n number of rows in the source data 
last_seven = df_exams.head(7)
print(last_seven)
# getting the shape attribute of the data frame
columsnandRows= df_exams.shape
print(columsnandRows)
# to get all the rows of the data frame
all= pd.set_option('display.max_rows', 1000)
print(df_exams)
# attributes-shape
first= df_exams.shape
print(first)
# getting access to the index 
index= df_exams.index
print(index)
# acccesing columns
c = df_exams.columns
print(c)
# accessing data type of each column
datatype= df_exams.dtypes
print(datatype)
# showing the information of the data frame
info= df_exams.info()
print(info)
#describing basic statistcs of the dataframe
describe_data= df_exams.describe()
print(describe_data)
# functions 
# obtaining the length of data frame number of rows
legnth= len(df_exams)
print(legnth)
#obtaining the highest index
highest= max(df_exams.index)
print(highest)
# obtaining the lowest  index 
lowest= min(df_exams.index)
print(lowest)
#obtaining the data frame 
typedataframe= type(df_exams)
print(typedataframe)
# rounding the value of dataset
# selecting one column - below is the most prefered one for all kind of column names including with those with two words 
gender= df_exams['gender']
print(gender)
# selecting two or more columns from dataframe
#select two columns using [[]]
towScore=df_exams[['gender','reading score']]
print(towScore)
# adding a new column to a data frame 
# addign a new column with a scalar value 
df_exams['language score']=70
print(df_exams)
# adding new columns with arrays
# import NumPy for arrays.
import numpy as np
language_score=np.arange(0,1000)

df_exams['language score']= language_score
print(df_exams)
# create random numbers between 1 and 100
language_score = np.random.randint(1,100, size =1000)
print(language_score)
df_exams['language_score']= language_score
print(df_exams)
# operation in column
sum_COlumn_reading_score= df_exams['reading score'].sum()
print(sum_COlumn_reading_score)
# sort a data frame
df_exams.sort_values(by='language score')
print(df_exams)
# sort descending by multiple columns 
sorted = df_exams.sort_values(by=['reading score','writing score'],ascending=True,inplace=True)
print(df_exams)



