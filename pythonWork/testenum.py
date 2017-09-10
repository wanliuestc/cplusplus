from enum import Enum, unique

class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(dir(Weekday))
print(Weekday.Sun)
for k in Weekday.__members__.items():
    print(k[1])

kw = {'123':'123'}
print(kw['123'])
