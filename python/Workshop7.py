# #1
# def draw_diamond(x):
#     for i in range(x):
#         if i <= x//2:
#             print(' '*(x//2-i)+'#'*(2*i+1))
#         else:
#             print(' '*(i-x//2)+'#'*(2*(x-i)-1))
#     return ''
# print(draw_diamond(7))





# #2
# def draw_diamond(x):
#     return '\n'.join([' '*(x//2-i)+'#'*(2*i+1) if i <= x//2 else ' '*(i-x//2)+'#'*(2*(x-i)-1) for i in range(x)])

# print(draw_diamond(9))

username = input("Enter your username: ")
print("Hello,", username,". Let's crete your grocery list.")

grocery_items = {}
while True:
    item = input("Enter the item(or 'done' to finish): ")
    if item == 'done':
        break
    price = int(input("Enter the price of product : "))
    grocery_items[item] = price

print("Your Grocert List:")
total_cost = 0
for item, price in grocery_items.items():
    print(f"{item}: {price}")
    total_cost += price

print("Total Cost: ", total_cost, "Baht")