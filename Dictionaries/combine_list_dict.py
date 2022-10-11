prices = {
    "arugula": 1.10,
    "basil": 2.54,
    "blackberries": 4.93,
    "blueberries": 2.88,
    "coconut": 7.15,
    "fennel": 3.36
}

produce = {
    "arugala": {
        "price": 1.10,
        "qty": 61,
        "is_organic": True,
        "producer": "Blue Kitty Farms"
    },
    "coconut": {
        "price": 7.15,
        "qty": 12,
        "is_organic": False,
        "producer": "Tropical Dream Farm"
    }
}

print(produce["coconut"]["producer"])

# nesting examples
test_scores = {
    "Marsha": [78, 80, 89],
    "Baker": [69, 65, 52]
}

waitlist = [
    {
        "email": "tiff@gmail.com",
        "location": "USA",
        "first_name": "Tiffany"
    },
    {
        "email": "tiff@gmail.com",
        "location": "USA",
        "first_name": "Tiffany"
    }
]
