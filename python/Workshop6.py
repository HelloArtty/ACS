def isPalindrome(x):
    x_str = str(x)
    return  x_str == x_str[::-1]
print(isPalindrome(12321))