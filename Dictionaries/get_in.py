prices = {
    "arugula": 1.10,
    "basil": 2.54,
    "blackberries": 4.93,
    "blueberries": 2.88,
    "coconut": 7.15,
    "fennel": 3.36
}

product = input("What product are you buying?\n> ")
if product in prices:
    price = prices[product]
    print()
    print(f"{product} is ${price}")
else:
    print()
    print("I don't have that - sorry!")
print()

## using in operator
print('fennel' in prices) # True
print('thai basil' in prices) # False
print(4.93 in prices) # False - in operator only looking at KEYS

print()

## .get() dictionary method
product = input("What product are you buying?\n> ")
price = prices.get(product)
if price:
    print()
    print(f"{product} is ${price}")
else:
    print()
    print("I don't have that today, sorry!")
