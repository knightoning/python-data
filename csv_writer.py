import csv

headers = ['A','B']

rows = [(1,4),(2,5),(3,6)]

# a+ 在原文件后追加字符，而不是覆盖原文
# w 覆盖原文
# open(参数1，参数2，参数3)
# 参数1：file文件路径；参数2：mode编写打开模式；参数3:encoding 文件的编码方式

f = open("TXT_COMMA2.txt",'w',encoding='utf-8')

wf = csv.writer(f)

# writerow 将数据写成一行
wf.writerow(headers)

# writerow 将数据写成多行
wf.writerows(rows)

f.close()