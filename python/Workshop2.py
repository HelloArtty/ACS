def find_perimeter(width,length):
    perimeter = 2*(width+length)
    return perimeter

width= int(input("Enter width: "))
length= int(input("Enter length: "))

print(find_perimeter(width, length))