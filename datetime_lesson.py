from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta

# d1 = date(2019, 3, 12)
# print(d1)
# print(d1.year)
# print(d1.month)
# print(d1.day)



# t1 = time(23, 59, 58)
# print(t1)
# print(t1.hour)
# print(date.today())
# print(date.max)
# print(datetime.today())
# print(datetime.now()) 

dt = datetime.strptime("30/08/2018 10:40", "%d/%m/%Y %H:%M")
print(dt)

delta1 = timedelta(days = 3, hours = 2, minutes = 10)
print(delta1)

delta2 = timedelta(days = 2, hours = 1, minutes = 5)
print(delta2)

birthday = date(2002, 12, 8)
delta = date.today()- birthday
myage = f"{delta.days//365} years, {delta.days%365} days"
print(myage)