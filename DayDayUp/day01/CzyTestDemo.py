# # 1. 数据类型 (类型转换 .每个类型常用方法, )
# #python的数据类型有1、字符串 2、布尔类型 3、整数 4、浮点数
# # 5、 数字 6、列表 7、元组 8、字典 9、日期
#
# #控制字符串循环（* 在数字中表示乘号，在字符串中表示重复多少次）
# e = '我爱中国 ,'*8
# print(e)
#
# #拆分字符串
# for g in 'I love china':
#     print(g)
#
# #字符串---用单引号或双引号括起来
# str = 'who are you ?'
# str2 = 'i am String'
# print(str+'  '+str2)
#
# #还有一种三引号，在三引号中可以自由使用单引号或双引号
# str3 = '''我说：“很高兴认识你”'''
# print(str3)
# #除了使用 ''' 来区分单引号和双引号外，还可以用转移字符 \ 来做区分
# print('我说：\"很高兴认识你\"')
# #转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# #使用r表示不让 \ 发生转义
# print('转义前：'+'i say \"my \name is jhon.\n\t what\'s your name? Milke \\ Allen\"')
# print('转义后：'+r'i say \"my \name is jhon.\t what\'s your name? Milke \\ Allen\"')
#
# #ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# #'%d'% X  表示将整型转换为字符串
# print('A的ASCII编码是： '+'%d' %ord('A'))
# print('中的ASCII编码是： '+ '%d' %ord('中'))
# print('66对应的字符是： '+ chr(66))
# print('25991对应的字符是： '+chr(25991))
# #r如果知道中文的ASCII编码，可以将其转化为16进制然后在打印出来
# print('该16进制的对应的字符是： '+'\u4e2d\u6587')
#
# #十进制转各种进制 ： bin()二进制 oct()八进制 hex()十六进制
# #将输入的中文转化为各种进制字符
# #获取用户输入的字符
# useWrord = str(input("请输入需要转化的文字： "))
# #循环字符串进行转码
# list2 = []
# list8 = []
# list16 = []
# for i in useWrord:
#      strCode = ord(i)
#      list2.append(bin(strCode))
#      list8.append(oct(strCode))
#      list16.append(hex(strCode))
# print('输入内容的转换为二进制是： ')
# print(list2)
# print('输入内容的转换为八进制是： ')
# print(list8)
# print('输入内容的转换为十六进制是： ')
# print(list16)
#
# #将字符串转换为一个整型
# x = '1'
# y = int(x)
# print(y)
#
# #整型转换为字符串
# a = 1
# b = '%d' %a
# print(a)
#
# # #将字符串转换为一个浮点型
# str4 = '4.1'
# c = float(str4)
# print(c)
#
# # #将浮点型转换为字符串
# d = 4.1021
# str5 = '%f'%d
# print((str5))
#
# #数字的基本应用
# print(2+1)
# print(2*2)
# print(16/2)
# print(15%6)
# print(2**5)
#
# # #获取长度
# print(len(str(2**1000000)))
#
# # 2 字符操作(截取 拼接,替换 等)
# testSente1 = '我 是中国 人，我爱中国!'
# testSente2 = '''i'm Chinese,i love China!'''
# testSente3 = 'HelloWord'
# #首字母大写
# print(testSente2.capitalize())
# #首字母小写
# print(testSente3.casefold())
# #字符串宽度填充，使用原有字符串+填充字符构成指定长度的新的字符串，数字为新生字符串的长度,注意python对大小写敏感
# #默认以空格返回
# print(testSente3.center(15))
# #以定义的填充物返回
# print(testSente3.center(16,'*'))
# #统计某个字符在字符串中出现的次数，或在字符串指定区间内完成上述操作
# print(testSente2.count('i'))
# print(testSente2.count('i',0,8))
# #对字符串进行编码操作
# print(testSente1.encode('gbk'))
# #判断字符串是不是以某个字符结束的,可以加个范围对字符串进行截取后判断
# print(testSente3.endswith('d'))
# print(testSente3.endswith('d',2,5))
# #判断字符串是不是以某个字符开始的
# print(testSente3.startswith('H'))
# #将制表符'\t'转换成指定宽度的tab键分割，默认tabsize=8
# li = 'sw\tht'
# print(li.expandtabs(16))
# #在字符串中查找指定字符串，找不到时返回-1,同样可以加上范围
# print(testSente2.find('C',0,3))
# #格式化输出的字符串
# li = 'I\'m {},{}' #两个'{}'是占位符
# print(li.format('swht','欢迎来中国'))
# #判断字符串中是否包含所找的字符串
# print(testSente2.__contains__('Chi'))
# # 在字符串中查找指定的字符串,找不到时直接报错,找到时返回位置
# print(testSente3.index('W'))
# #字符串连接
# #把join里面的字符串拆分后和原来的字符串组合成新的
# print(testSente3.join('*********'))
# print(''.join(testSente2))
# str_list = ['love', 'Python']
# print('通过join形式连接 ：' + ''.join(str_list) + '\n')
# #通过 + 来连接
# print(testSente1+testSente3)
# #通过 ， 来连接
# print(testSente3,testSente2)
# #直接连接
# print('直接连接这种方式' '好像只能用引号')
# #格式化连接
# print('通过格式化形式连接 ：' + '%s %s' % ('love', 'Python') + '\n')
# #检查判断字符串是否包含字母数字字符
# print(testSente1.isalnum())
# #检测字符串是否只由字母组成
# print(testSente3.isalpha())
# #检测字符串是否只由数字组成
# print(testSente3.isdecimal())
# #检测字符串是否是字母开头
# #为什么这里打印false
# print(testSente2)
# print(testSente2.isidentifier())
# #检测字符串是否由数字组成
# print(testSente3.isnumeric())
# #判断字符串中所有字符是否都属于可见字符,及时判断字符串中是不是又转义符
# testSente4 = '\t这里是有转义符的'
# print(testSente4.isprintable())
# #判断字符串是不是为空字符串
# print(testSente3.isspace())
# #判断字符串是否适合当作标题（其实就是每个单词首字母大写）,不允许首字母外其他地方有大写
# testSente5 = 'Aaa'
# print(testSente5.istitle())
# #判断字符串中所有字母字符是否都是大写字母
# print(testSente3.isupper())
# #根据指定的分隔符将字符串进行分割。
# print(testSente2.partition(','))
# #把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# str = "this is string example....wow!!! this is really string"
# str1= str.replace("is", "was")
# print('原来的句子： '+str)
# print('转换后的句子： '+str1)
# str1= str.replace("is", "was",3)
# print('加了最大次数转换后的句子： '+str1) #注意单替换时遇到字符串中有替换字符则被旧的字符替换
# #字符串分割，默认是空格
# print(testSente2.split())
# #在字符串后面增加指定的字符或字符串
# print(testSente2.__add__(' How are you'))
# #判断字符串是不是相等
# print(testSente2.__eq__(testSente1))
# #对字符串进行分割后返回一个列表
# testSente6 = '''I have a pen \r\n I have a apple
# apple pen'''
# testlist = testSente6.splitlines()
# print(testlist)



