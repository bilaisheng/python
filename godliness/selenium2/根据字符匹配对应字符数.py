from pip._vendor.distlib.compat import raw_input

str = ''
while True:

    input = raw_input("请输入字符：")
    if input == "quit":
        break
    else:
        str += input

letters = 0
space = 0
digit = 0
others = 0

for i in str:
    if i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    elif i.isalpha():
        letters += 1
    else:
        others += 1

print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))