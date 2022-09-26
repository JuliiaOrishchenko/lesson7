stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_stock = {}
for fruit, quantity in stock.items():
    if fruit in prices:
        total_stock[fruit] = int(stock[fruit]*int(prices[fruit]))
print(total_stock)
