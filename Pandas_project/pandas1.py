import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9],[1,2,3]],    columns=["A","B","c",],  index=["a","b","c","d"])
#print(df)                              #Printing the data
#print(df.head(2))                      #Open data in upper side
#print(df.tail(1))                      #Open data in down side
#print(df.columns)                      #show the columns
#print(df.index)                        #show the indexing
#print(df.info())                       #show the information of data
#print(df.describe())                   
#print(df.nunique())                    #show the number of each columns
#print(df["A"].unique)                  #print only specify column
#print(df.shape)                        #show the shape of data
#print(df.size)                         #show the number of data
