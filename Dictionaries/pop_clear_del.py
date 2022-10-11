prices = {
    "arugula": 1.10,
    "basil": 2.54,
    "blackberries": 4.93,
    "blueberries": 2.88,
    "coconut": 7.15,
    "fennel": 3.36
}

## .pop()
print(prices.pop('coconut')) # 7.15
print(prices) # list without coconut key

## .popitem()
print(prices.popitem()) # ('fennel', 3.36)
    # returns a tuple
print(prices)

prices["orange"] = 1.35
prices.popitem()
print(prices) # orange removed

## .clear() deletes all items from a dictionary

## del command (NOT method) can clear full dict or individual key-value pair
del prices["arugula"]
print(prices)
    # arugula is removed
