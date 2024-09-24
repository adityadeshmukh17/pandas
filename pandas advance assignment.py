# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
import pandas as pd
# Values=[10,20,30,40,50]
# k=pd.Series(Values)
# # print(type(k))
# df=pd.DataFrame(k)
# # print(df[0])
# sum=0
# for j in range(3):
#     sum+=df[0][j]
# print(sum)

# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.
# Text=['ans','sns','yeye']
# Word_Count=[1,2,3]
# df=pd.DataFrame({'Text':Text,'Word_Count':Word_Count})
# st=(df.loc[0,['Text']])
# for j in range(len(df['Text'])):
#     st=len(df.loc[j,['Text']][0])
#     df['Word_Count'][j]=st
# print(df)

# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.
# a=['adi@gmai.com','sad@gmail.com']
# b=['a','b']
# s=pd.Series(a)
# df=pd.DataFrame({'Email':s,'Username':b})
# z=[]
# for j in df['Email']:
#     ans=''
#     for k in j:
#         if k=='@':
#             break
#         ans+=k
#     z.append(ans)
# df['Username']=z
# print(df)

# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# A=[3,8,6,2,9]
# B=[5,2,9,3,1]
# C=[1,7,4,5,2]
# df=pd.DataFrame({'A':A,'B':B,'C':C})        
# print(df)
# # print(df['A']>5 & df['B']<10)
# print(df[(df['A']>5) & (df['B']<10)])

# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.
# For example, if df contains the following values:
# Date
# 0 2023-01-01
# 1 2023-01-02
# 2 2023-01-03
# 3 2023-01-04
# 4 2023-01-05
# Your function should create the following DataFrame:

# Date Weekday
# 0 2023-01-01 Sunday
# 1 2023-01-02 Monday
# 2 2023-01-03 Tuesday
# 3 2023-01-04 Wednesday
# 4 2023-01-05 Thursday
# The function should return the modified DataFrame.
# Date=['2023-01-01','2023-01-02','2023-01-03','2023-01-04']
# df=pd.DataFrame({'Date':Date})
# df['Weekday']='null'
# print(df)
# for j in range(len(df['Date'])):
#     for k in df['Date'][j]:
#         if k[-1]=='1':
#             df['Weekday'][j]='sunday'
#         elif k[-1]=='2':
#             df['Weekday'][j]='monday'
#         elif k[-1]=='3':
#             df['Weekday'][j]='tuesday'
#         elif k[-1]=='4':
#             df['Weekday'][j]='wednesday'
#         elif k[-1]=='5':
#             df['Weekday'][j]='thursday'
#         elif k[-1]=='6':
#             df['Weekday'][j]='friday'
#         else:
#             df['Weekday'][j]='saturday'
# print(df)


# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.
# Date=['2023-01-03','2023-01-02','2023-01-01','2023-01-04']
# df=pd.DataFrame({'Date':Date})

# # print(int(df['Date'][-2::1])>1 and int(df['Date'][-2::1])<4)
# list=[]
# for j in range(len(df['Date'])):
#     if int(df['Date'][j][-2::1])>1 and  int(df['Date'][j][-2::1])<31:
#         list.append(j)
# list.sort()
# # print(list)
# print(df['Date'][list])
# print(df['Date'][[0,1,3]])

# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.
# Values=[1,2,3,4,5,5]
# df=pd.DataFrame({'Values':Values})
# print(df)
# print(type(df.describe()))
# print(df.describe()['Values'][['mean','std','50%']])

Date=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
Sales=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
movingavg=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
df=pd.DataFrame({'date':Date,'sales':Sales,'moving avg':movingavg})
print(df)
for j in range(14):
    df['moving avg'][j]=sum(df['sales'][j:j+7])/7
print(df)