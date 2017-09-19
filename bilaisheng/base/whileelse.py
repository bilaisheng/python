
# 你可以使用 CTRL+C 来退出当前的无限循环。
# 无限循环在服务器上客户端的实时请求非常有用。

count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")