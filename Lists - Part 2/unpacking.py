item = [4, "Pizza", "Plain", 16.98]

quantity, *others, price = item
print(quantity, others, price) # others is stored as list

race_results = ['bill', 'ted', 'tammy', 'jimbo', 'billybob', 'pierre']
gold, silver, bronze, *losers = race_results

print(gold, silver, bronze, losers)
