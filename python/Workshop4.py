# def group_fruits_and_vegetables(items_list):

#     fruits = [ ]
#     vegetables = []
#     for item in items_list:
#         if is_fruit(item):
#             fruits.append(item)
#         elif is_vegetable(item):
#             vegetables.append(item)
#         else:
#             print("Warning: 'shoes' is neither a fruit nor a vegetable!")

#     grouped_dict = {
#                 'fruits': fruits,
#                 'vegetables': vegetables
#     }

#     return grouped_dict

# def is_fruit(item):
#     fruits_list = ['apple','banana','orange','mango','strawberry']
#     return item.lower() in fruits_list

# def is_vegetable(item):
#     vegetables_list = ['carrot','broccoli','tomato','spinach','cucumber']
#     return item.lower() in vegetables_list

# items_list = ['Apple','Banana','Orange','Mango','shoes','Carrot','Broccoli','Tomato','Spinach']
# print(group_fruits_and_vegetables(items_list))



def calculate_total_price(vegetables_and_fruits_prices, shopping_list):
    total_price = 0
    for item in shopping_list:
        if item in vegetables_and_fruits_prices:
            total_price += vegetables_and_fruits_prices[item]
        else:
            print(f'ไม่พบรายการ "{item}" ในรายการผักและผลไม้')
    return total_price


vegetables_and_fruits_prices = {
    'apple': 50,
    'banana': 20,
    'orange': 15,
    'mango': 30,
    'carrot': 25,
    'broccoli': 17,
    'tomato': 10,
    'spinach': 30,
    'cucumber': 15,

}

shopping_list = ['apple','banana','broccoli','cucumber', 'mango']

total_price = calculate_total_price(vegetables_and_fruits_prices, shopping_list)
print('ราคารวม คือ',total_price,'บาท')