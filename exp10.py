''' Data preprocessing '''
# Creating Dataframe
import pandas as p
import numpy as n
Data = {'H': [1, n.nan, 7], 'I': [2, 5, n.nan], 'E': [3, 6, 9]}
Df = p.DataFrame(Data)
print(Df)
'''Methods For Data Pre-Processing'''
# 1.Drop Missing Values
Df_drop = Df.dropna()
print(f"data frame after dropping missing values:\n {Df_drop}")
# 2. Fill missing values with mean of column
Df_fill = Df.fillna(Df.mean())
print(
    f"data frame after filling missing values with mean of column:\n {Df_fill}")
# 3.Fill with Specific value
Df_specific = Df.fillna(0)
print(f"Dataframe after filling with specific value:\n{Df_specific}")
# 4.forward fill
Df_forward = Df.fillna(method='ffill')
print(f"Dataframe after forward fill:\n{Df_forward}")
# 5.Backward Filling
Df_backward = Df.fillna(method='bfill')
print(f"Dataframe after backward fill:\n{Df_backward}")
'''Handling categorized data'''
# one hat encoding
data = {'names': ['pawan', 'mahesh', 'charan', 'mahesh', 'pawan']}
df = p.DataFrame(data)
encoding = p.get_dummies(df['names'])
df = p.concat([df, encoding], axis=1)
df = df.drop('names', axis=1)
print(df)
