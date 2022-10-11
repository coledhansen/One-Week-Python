def get_total(price, qty = 1, tax = 0.02, discount = 0):
    subtotal = price * qty * (1-discount)
    print(subtotal * (1 + tax))

get_total(4.99, 5, 0.015, 0.2)
get_total(price = 4.99, qty = 5, tax = 0.015, discount = 0.2)
    # prints the same output

get_total(price = 9.75, qty = 5, discount = 0.2) # providing value for args
    # in this case it is defaulting the tax rate since it is not passed

# error
# get_total(tax = 0.025, 8.99) # positional arg follows keyword arg
get_total(tax = 0.025, price=8.99) # will work
