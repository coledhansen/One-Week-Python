tweet = len(input("Enter your tweet here:\n> "))
max_chars = 140
checker = tweet - max_chars

if tweet < max_chars:
    print(f"That {tweet} char tweet will work!")
elif tweet > max_chars:
    print(f"Your {tweet} char tweet is {checker} chars too long.")
else:
    print(f"Your tweet is exactly {max_chars} char long. Good job!")
