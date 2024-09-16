import pandas as pd
# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.
# a=[4, 8, 15, 16, 23,42]
# s=pd.Series(a)
# print(s)

# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.
# a=[1,2,3,4,5,6,7,8,9,10]
# b=pd.Series(a)
# print(b)

# # Q3. Create a Pandas DataFrame that contains the following data:
# def create(d,col):
#     df=pd.DataFrame(d,columns=col)
#     return df
# d=[['alice',25,'female'],['bob',30,'male'],['claire',27,'female']]
# col=['name','age','gender']
# df=create(d,col)
# print(df)

s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])
df = pd.DataFrame({'A': s1, 'B': s2})

print(df)