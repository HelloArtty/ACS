# quest1_input = int(input("Enter the list of numbers: "))
# def find_max_height(t):
#     g = 9.8
#     H = (t**2)*g/8
#     return H

# print("%.2f"%find_max_height(quest1_input))


def find_perimeter(width,length):
    perimeter = 2*(width+length)
    return perimeter

width= int(input("Enter width: "))
length= int(input("Enter length: "))

print(find_perimeter(width, length))