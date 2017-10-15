def hello():
    print("这是一个无参数的方法！")

hello();


print("")

def  helloOne(str):
    print(str);

helloOne("一个带参数的字符串！")

print("")

#带有默认值的参数
#若直接调用helloTwo()不传参数 ，使用该方法参数默认值 ，否则使用传入参数
def helloTwo(age = 35):
    print(age)

helloTwo(50);

def area(width=50,height=60):
    return width * height

print(area(200,200))

