import pandas as pd

df = pd.read_csv(open("Customer Call List.csv"))

Coffee=pd.read_csv(open('Coffee.csv'))
#print(df.
# drop_duplicates())
#
#df_1=df.drop_duplicates()
#df_2=df["CustomerID"]<1005
#df_3=["Frodo"]
#print([df["First_Name"].st.contains("frodo")])

#print(Coffee["Units Shold"]>25)
#print(Coffee["Coffee Type"].str.contains("Latte"))

#print(Coffee.set_index('Day'))

#print(Coffee.filter(type='Coffee Type'))
df_=df+Coffee
print(df)