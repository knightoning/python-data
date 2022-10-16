from pandas import Series

s = Series([1,2,'aa','b'])

print(s)

#替换下标1的值
s[1]=3

print(s)

s1 = Series([1,2,'aa','b'],index = ['A','bb','c','D23'])

s2 = Series([111,234,'AA'])

s2.index = ['A','bb','c']

print(s1)
print(s2)
