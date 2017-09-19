# 导入datetime模块，用以操作时间
import datetime
# 导入time模块
import time


# 获取当前时间 格式： 年-月-日  时：分：秒 . 毫秒
nowTime = datetime.datetime.now()
print('当前时间格式： 年-月-日  时:分:秒.毫秒 为：' + str(nowTime) + "\n")
print('当前时间格式： 年-月-日 : ' + str(datetime.date.today()) + '\n')


# 获取时间戳  timestamp  格式： 秒.毫秒
print('当前时间戳为 : ' + str(time.time()) + "\n")


# 获取元组格式时间
print('元组格式时间 :' + str(time.localtime()) + "\n")


# 格式化时间
print('格式化后的当前时间为: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')


# 根据传入年月日输入时间
# Tips: 若月 日 等小于10  请输入 对应数字不可前面补0  如九月  请填写9 不可以为09
print('根据传入年月日输入时间 : ' + str(datetime.date(2017, 6, 30)) + '\n')

# 获取前N天的日期
# Tips : days= 第N天 可跨年计算
# +:之后多少天   - : 之前多少天
print('第200天之前为 : ' + str(datetime.datetime.today()-datetime.timedelta(days=200)) + '\n')


# 两个日期差 单位: 秒
print("两个日期差为 : " + str((datetime.datetime(2017, 12, 13, 12, 0, 0) - datetime.datetime.now()).total_seconds()) + '秒\n')


# 本月1号
print('本月1号为: ' + str(datetime.date(datetime.date.today().year, datetime.date.today().month, 1)) + '\n')
# 等同于
print('本月1号为: ' + str(datetime.date.today().replace(day=1)) + '\n')
# 上月1号
print('上月1号为: ' + str((datetime.date.today().replace(day=1) - datetime.timedelta(1)).replace(day=1)) + '\n')


# 获取本周最后一天日期
today = datetime.datetime.today()
print('本周最后一天为 : ' + str(today + datetime.timedelta(6 - today.weekday())) + '\n')


# 上个月最后一天  ：当前月第一天-1天  获取上个月最后一天
# 获取当月第一天
firstDay = datetime.date(day=1, month=today.month, year=today.year)
lastMonth = firstDay - datetime.timedelta(days=1)
print('上个月最后一天为 : ' + str(lastMonth) + '\n')

'''
字符串格式化参数列表：
datetime. strftime (format)  
%a:  星期的简写。如 星期三为Web  
%A:  星期的全写。如 星期三为Wednesday  
%b:  月份的简写。如4月份为Apr  
%B:  月份的全写。如4月份为April   
%c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）  
%d:  日在这个月中的天数（是这个月的第几天）  
%f:  微秒（范围[0,999999]）  
%H:  小时（24小时制，[0, 23]）  
%I:  小时（12小时制，[0, 11]）  
%j:  日在年中的天数 [001,366]（是当年的第几天）  
%m:  月份（[01,12]）  
%M:  分钟（[00,59]）  
%p:  AM或者PM  
%S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）  
%U:  周在当年的周数当年的第几周），星期天作为周的第一天  
%w:  今天在这周的天数，范围为[0, 6]，6表示星期天  
%W:  周在当年的周数（是当年的第几周），星期一作为周的第一天  
%x:  日期字符串（如：04/07/10）  
%X:  时间字符串（如：10:43:39）  
%y:  2个数字表示的年份  
%Y:  4个数字表示的年份  
%z:  与utc时间的间隔 （如果是本地时间，返回空字符串）  
%Z:  时区名称（如果是本地时间，返回空字符串）  
%%:  %% => %
'''

