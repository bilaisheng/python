"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


def leno(s):
    """
    :type s: str
    :rtype: int
    """
    a = list(s)
    b = ''
    r = []
    s = ''
    for i in a:
        print(i)
        if i in b:
            r.append(b)
            print(b.index(i))
            b = b[b.index(i)+1:]
            print(i)
            b += i
            print(b)
        else:
            b += i
            print(b)
    r.append(b)
    print(max([len(k) for k in r]))

    return max([len(k) for k in r])