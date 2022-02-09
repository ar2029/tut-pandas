## importing the libraries
import pandas as pd
import sqlalchemy

# creating a list consist of special characters
specialChar = ['!','@','#','$','%','^','&','*','(',')']

## defining a function which replaces the special character
def formatString(st):
    for i in specialChar:
       st=st.replace(i,'')
    return st

## reading a csv file
df = pd.read_csv('C:\\Users\\Hp\\Desktop\\sample.csv')

# print(df[df['Item Type']=='Vegetables'])
# a = df.replace(to_replace='Vegetables', value='Fruits')
# df['new_column']='xyz'

## connecting to database engine by creating engine function which take follow
engine = sqlalchemy.create_engine('postgresql://postgres:root@127.0.0.1:5432/postgres')

# print(type(b[0]))
# df1 = pd.read_sql('SELECT * FROM abc.pdsample', engine)

df['Order ID']=[formatString(i) for i in df['Order ID']]
df['Country']=[formatString(i) for i in df['Country']]
df['Ship Date']=[formatString(i) for i in df['Ship Date']]
dfnew = df[['Order ID', 'Country', 'Ship Date']]

# for i in b:
#     for j in i:
#         if j not in '''!@#$%^&*()_+''':
#             z = z + j
# print(z)    

dfnew.to_sql('pdsample', con=engine, schema='abc',if_exists='replace', index=False)
dfnew.to_json('C:\\Users\\Hp\\Desktop\\sam.json', index=False)