#1

def draw_diamond(x):
    for i in range(x):
        if i <= x//2:
            print(' '*(x//2-i)+'#'*(2*i+1))
        else:
            print(' '*(i-x//2)+'#'*(2*(x-i)-1))
    return ''
print(draw_diamond(7))



#2

def draw_diamond(x):
    return '\n'.join([' '*(x//2-i)+'#'*(2*i+1) if i <= x//2 else ' '*(i-x//2)+'#'*(2*(x-i)-1) for i in range(x)])

print(draw_diamond(9))