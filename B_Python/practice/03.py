# 题目：输入某年某月某日，判断这一天是这一年的第几天？
from pip._vendor.distlib.compat import raw_input

year = int(raw_input("year:"))
month = int(raw_input("month:"))
day = int(raw_input("day:"))

#每月第一天
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

if 0 <= month <= 12:
    sum = months[month - 1]
else:
    print("data error !")

#获取当前总天数
sum += day

# 判断是否为闰年
leap = False

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = True
    if leap is True and month == 2:
        sum += 1

print("您输入的日期为"+str(year)+"年的"+str(sum)+"天!")