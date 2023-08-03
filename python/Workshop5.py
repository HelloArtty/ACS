
#1

def reverseString(s):
    new_String = ''
    for i in range(len(s)- 1, -1, -1):
        new_String += s[i] 
    return new_String

my_String = 'etuc os uoy'
my_String = reverseString(my_String)  
print(my_String)



#2

def reverseString(s):
    new_string = s[::-1]
    return new_string

my_String = 'etuc os uoy'
my_String = reverseString(my_String)  
print(my_String)