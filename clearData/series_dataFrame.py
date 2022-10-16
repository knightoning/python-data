from pandas import Series,DataFrame

data = {"title":['语文','数学','英语'],"score":[100,99,99]}

df = DataFrame(data)
print(df)

df = DataFrame(data, columns=['score','title'],index=['0','a','45'])
print(df)

data = {"title":{'A':'语文','B':'数学','C':'英语'},"score":{'A':100,'B':99,'C':99}}

df1 = DataFrame(data)
print(df1)

df1['score'] = [90,80,85]

df2 = df1.copy()

df2.at['C','score'] = 66
print(df2)



