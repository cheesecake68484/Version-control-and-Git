# List of items in menu
menu = ['Tea', 'Coffee', 'Doughnut', 'Muffin']
# Dictionary containing the stock value for each item
stock = {'Tea': 200,
         'Coffee': 200,
         'Doughnut': 100,
         'Muffin': 50
        }
# Dictionary containing the price of each item
price = {'Tea': 1,
         'Coffee': 2,
         'Doughnut': 1.50,
         'Muffin': 1
        }
# Initialize variable, iterate through stock dict. calculate total stock worth
item_value = 0
for items in stock:
    item_value += (stock [items] * price [items])
total_stock = item_value
# Print the value of all the stock
print(f"The total stock value is: £{total_stock}")

# I don't understand what the purpose of the menu list is ?
