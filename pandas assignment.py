# Consider following code to answer further questions:
# import pandas as pd
# course_name = [‘Data Science’, ‘Machine Learning’, ‘Big Data’, ‘Data Engineer’]
# duration = [2,3,6,4]
# df = pd.DataFrame(data = {‘course_name’ : course_name, ‘duration’ : duration})
# Q1. Write a code to print the data present in the second row of the dataframe, df.
import pandas as pd
import matplotlib.pyplot as py
course_name = ['Data Science', 'Machine Learning', 'Big Data', 'Data Engineer']
duration = [2,3,6,4]
df = pd.DataFrame(data = {'course_name' : course_name, 'duration' : duration})
# print(df)
# print(df.loc[2,['course_name','duration']])

# Q3. Reindex the given dataframe using a variable, reindex = [3,0,1,2] and store it in the variable, new_df
# then find the output for both new_df.loc[2] and new_df.iloc[2].
reindex=[3,0,1,2]
new_df=pd.DataFrame(df,index=reindex)
# print(new_df)
# print(new_df.loc[2])
# print(new_df.iloc[2])
# the difference is in accessing the rows.In loc it does based on named indexes and in iloc based on in built index

# Consider the below code to answer further questions:
# Q4. Write a code to find the following statistical measurements for the above dataframe df1:
# (i) mean of each and every column present in the dataframe.
# (ii) standard deviation of column, ‘column_2’
import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
# df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
# print(df1[['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']].mean())
# print(df1['column_2'].std())

# Q5. Replace the data present in the second row of column, ‘column_2’ by a string variable then find the
# mean of column, column_2.
# If you are getting errors in executing it then explain why.
# [Hint: To replace the data use df1.loc[] and equate this to string data of your choice.]
# df1.loc[2,['column_2']]='pwskillss'
# print(df['column_2'].mean())
# error due to the column containes mixed datatype

# Q7. Write a code to print only the current month and year at the time of answering this question.
# [Hint: Use pandas.datetime function]
# df=pd.DataFrame(['2023-8-19'])
# df['new']=pd.to_datetime(df[0])
# print(df['new'].dt.year)
# print(df['new'].dt.month)

# dates=[]
# for j in range(2):
#     date=input(f'enter date {j+1}')
#     dates.append(date)
# dates=['2023-8-8','2023-8-9']
# df=pd.DataFrame({'dates':dates})
# df['datesnew']=pd.to_datetime(dates)
# t=pd.Timedelta(hours=7,minutes=45)
# t1=pd.Timedelta(hours=9,minutes=35)
# df.iloc[0,[1]]=df.iloc[0,[1]]+t
# df.iloc[1,[1]]=df.iloc[1,[1]]+t1
# print(df)
# print(df['datesnew'].dt.day[1]-df['datesnew'].dt.day[0])
# print(df['datesnew'].dt.hour[1]-df['datesnew'].dt.hour[0])
# print(df['datesnew'].dt.minute[1]-df['datesnew'].dt.minute[0])

# Q9. Write a Python program that reads a CSV file containing categorical data and converts a specified
# column to a categorical data type. The program should prompt the user to enter the file path, column
# name, and category order, and then display the sorted data.
# df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(pd.Categorical(df['Pclass']))
# print(df.head())
# print(df.sort_values('Pclass',inplace=True))


# Q10. Write a Python program that reads a CSV file containing sales data for different products and
# visualizes the data using a stacked bar chart to show the sales of each product category over time. The
# program should prompt the user to enter the file path and display the chart.
# df=pd.read_csv("supermarket_sales - Sheet1.csv")
# g=df.groupby('Product line')
# y1=list(g.sum()['Total'])
# x1=list(df['Product line'].unique())
# df1=pd.DataFrame({'product line':x1,'total':y1})
# df1.plot(kind='bar',x='product line',y='total')
# py.show()

# Q11. You are given a CSV file containing student data that includes the student ID and their test score. Write
# a Python program that reads the CSV file, calculates the mean, median, and mode of the test scores, and
# displays the results in a table.
# The program should do the followingM
# I Prompt the user to enter the file path of the CSV file containing the student dataR
# I Read the CSV file into a Pandas DataFrameR
# I Calculate the mean, median, and mode of the test scores using Pandas toolsR
# I Display the mean, median, and mode in a table.
# Assume the CSV file contains the following columnsM
# I Student ID: The ID of the studentR
# I Test Score: The score of the student's test.
# Example usage of the program:
# Enter the file path of the CSV file containing the student data: student_data.csv
# +-----------+--------+
# | Statistic | Value |
# +-----------+--------+
# | Mean | 79.6 |
# | Median | 82 |
# | Mode | 85, 90 |
# +-----------+--------+
# Assume that the CSV file student_data.csv contains the following data:
# Student ID,Test Score
# 1,85
# 2,90
# 3,80
# 4,75
# 5,85
# 6,82
# 7,78
# 8,85
# 9,90
# df1=pd.DataFrame({
#     'id':[1,2,3,4,5,6,7,8,9,10],
#     'scores':[11,33,33,44,55,66,77,88,33,100]
# })
# median=(df1['scores'].median())
# mode=(df1['scores'].mode())
# df1=df1.describe().loc[['mean','50%'],['scores']]
# df1.loc['mode',['scores']]=mode[0]
# print(df1)


