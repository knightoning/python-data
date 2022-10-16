import csv


with open("TXT_COMMA.txt") as cf:

     lines = csv.reader(cf)

     for line in lines:

     	print(line)
