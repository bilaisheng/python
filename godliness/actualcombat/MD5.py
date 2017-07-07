# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作


import hashlib

# 待加密信息
str = 'this is a md5 test.'

# 创建md5对象
hl = hashlib.md5()

# Tips
# 此处必须声明encode
# 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
hl.update(str.encode(encoding='utf-8'))

print('MD5加密前为 ：' + str)
print('MD5加密后为 ：' + hl.hexdigest())

# 生成MD5
def genearteMD5(str):
    # 创建md5对象
    hl = hashlib.md5()

    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding='utf-8'))

    print('MD5加密前为 ：' + str)
    print('MD5加密后为 ：' + hl.hexdigest())

