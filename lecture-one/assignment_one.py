'''
    Write a Python program that can do the following:

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
'''


current_balance = 50
print(f"You have current balance: {current_balance}")
item_cost = 15
item_tax = (item_cost * 3) / 100
total_item_cost = item_cost + item_tax

current_balance = current_balance - total_item_cost
print(f"You have current balance: {current_balance}")