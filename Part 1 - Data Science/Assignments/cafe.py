#create a list called menu
menu = ['espresso',
        'drip coffee',
        'muffin',
        'brownie',
        'hot chocolate']

#create a dictionary called stock
#has the value of total stock of each item

stock = {'espresso': 600,
         'drip coffee': 200,
         'muffin': 100,
         'brownie': 200,
         'hot chocolate': 100}

#create a dictionary with the price of each item on menu

price = {'espresso': 1.00,
         'drip coffee': 0.50,
         'muffin': 1.00,
         'brownie': 1.00,
         'hot chocolate': 2.00}

#setting the total stock to = 0
total_stock = 0 

for item, value in stock.items():
    value_per_item = (stock[item] * price[item])
    total_stock += value_per_item

print(f'The total value of the stock is $ {total_stock:.2f}')





