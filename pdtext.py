import sys
# import pandas as pd
# df = pd.read_fwf('C:\\Users\\Hp\\Desktop\\sample.txt')
# print(df)
# # df.to_csv('C:\\Users\\Hp\\Desktop\\sampletxt.csv', index=False)

# df1 = pd.read_json('C:\\Users\\Hp\\Desktop\\sample.json')
# print(df1)

sys.setrecursionlimit(10**6) 


def fun(n):
    #1+(1/fun(n))
    if n == 8:
        return(1 + (1/2))
        
    else:
        return(1+(1/fun(n+1)))

print(fun(1))

def abc():
    c = 2 + 2
    return c

print(abc())
