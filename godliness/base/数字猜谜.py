number = 7
guess = 10

print("猜字游戏开始！！")

while guess != number:
    guess = int(input("请输入您要猜的数字："))

    if guess == number:
        print("恭喜您猜对了")
    elif guess < number:
        print("您猜的太小了")
    elif guess > number:
        print("您猜的太大了")

###  退出游戏
input("点击 Enter 退出！");