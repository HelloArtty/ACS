def find_thing(list):
    fruits = ['Apple','Banana','Orange','Mango','Strawberry']
    vegetable = ['Carrot','Broccoli','Tomato','Spinach','Cucumber']
    result = 0
    for i in range(len(list)):
        if list[i] in vegetable:
            result += 1
    return result

list = ['Apple','Banana','Broccoli','Cucumber','Mango','Strawberry']
print(find_thing(list))