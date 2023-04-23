from datetime import date
import datetime

f_date = date(2014, 7, 2)
l_date = date(2015, 7, 11)
delta = l_date - f_date
now = datetime.datetime.now()

print(delta)
print(f_date)
print(now)
print(type(delta))
print(type(f_date))
print(type(now))