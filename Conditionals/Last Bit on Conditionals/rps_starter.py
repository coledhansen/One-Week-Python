from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    comp = rock
elif num == 2:
    comp = paper
elif num == 3:
    comp = scissors


# Ask a user to enter their move
move = input("enter your move:\n> ")
print()
if move == 'rock':
    move = rock
elif move == 'paper':
    move = paper 
elif move == 'scissors':
    move = scissors

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("YOUR MOVE:")
print(move)

print()

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("COMPUTER MOVE:")
print(comp)

if comp == rock:
    comp = 'rock'
elif comp == paper:
    comp = 'paper'
elif comp == scissors:
    comp = 'scissors'

# convert back
if move == rock:
    move = 'rock'
elif move == paper:
    move = 'paper'
elif move == scissors:
    move = 'scissors'

# Figure out who wins and print the result!
if move == 'rock' and comp == 'scissors':
    print("you win!")
elif move == 'rock' and comp == 'rock':
    print("it's a tie!")
elif move == 'rock' and comp == 'paper':
    print("you lose!")

if move == 'scissors' and comp == 'scissors':
    print("it's a tie!")
elif move == 'scissors' and comp == 'rock':
    print("you lose!")
elif move == 'scissors' and comp == 'paper':
    print("you win")

if move == 'paper' and comp == 'scissors':
    print("you lose!")
elif move == 'paper' and comp == 'rock':
    print("you win!")
elif move == 'paper' and comp == 'paper':
    print("it's a tie!")
