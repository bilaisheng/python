# 引入日历模块
import calendar

#指定年月
yy = int(input("请输入年份："))
mm = int(input("请输入月份："))

# 显示日历
print(calendar.month(yy, mm))