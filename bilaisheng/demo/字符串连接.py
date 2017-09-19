
# 字符串连接的五种方式

# 第一种 通过加号(+)的形式
print('第一种方式通过加号形式连接 ：' + 'love'+'Python' + '\n')

# 第二种 通过逗号(,)的形式
print('第二种方式通过逗号形式连接 ：' + 'love', 'Python' + '\n')

# 第三种 直接连接  中间有无空格均可
print('第三种方式通过直接连接形式连接 (一) ：' + 'love''Python' + '\n')
print('第三种方式通过直接连接形式连接 (二) ：' + 'love'    'Python' + '\n')


# 第四种 格式化
print('第四种方式通过格式化形式连接 ：' + '%s %s' % ('love', 'Python') + '\n')

# 第五种 join方式连接
str_list = ['love', 'Python']
print('第误种方式通过join形式连接 ：' + ''.join(str_list) + '\n')

