

def isPalindrome(x):
    if x < 0:
        return False
    tmp = x
    y = 0
    while tmp:
        y = y * 10 + tmp % 10
        print(y)
        tmp = tmp / 10
    return y == x

print(isPalindrome(303))