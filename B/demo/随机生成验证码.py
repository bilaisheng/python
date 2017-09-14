
import random

def generate_verification_code_two():
    '''随机成成6位验证码'''
    code_list = []

    for i in range(1,3):
        # 随机成成0-9之间的数字
        random_num = random.randint(0, 9)
        # 利用random生成65-90之间的随机整数 使得65<=a<=90
        # 对应从'A'到'Z'之家的ASCII码
        a = random.randint(65, 90)
        # 对应从'a'到'z'之家的ASCII码
        b = random.randint(97, 120)

        random_uppercase_letter = chr(a)
        random_lowercase_letter = chr(b)

        code_list.append(str(random_num))
        code_list.append(random_uppercase_letter)
        code_list.append(random_lowercase_letter)
    verification_code = ''.join(code_list)
    return verification_code

print(generate_verification_code_two())





def generate_verification_code(len=6):
    ''' 随机生成6位的验证码 '''
    # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
    # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # 对应从“A”到“Z”的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123): #对应从“a”到“z”的ASCII码
        code_list.append(chr(i))
    myslice = random.sample(code_list, len)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code

print(generate_verification_code())
