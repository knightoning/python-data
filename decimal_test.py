from  decimal  import *

print(getcontext())

getcontext().prec = 50

print(Decimal(1) / Decimal(9))

print(Decimal(1) / Decimal(19))

print(float(Decimal(1) / Decimal(10)))