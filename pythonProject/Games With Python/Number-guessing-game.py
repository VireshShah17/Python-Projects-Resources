#Day 12 Project
#Number Guessing Game

import random
def game(number_of_attempt):
  play = True
  while play:
    print(f"You have {number_of_attempt} attemp to guess.")
    if number_of_attempt == 0:
      print(f"You lose,the number was {comp_number}")
      play = False
      break
    user_number = int(input("Make your guess"))
    if user_number > comp_number:
      print("Too high.")
      number_of_attempt -= 1
      play = True
    elif user_number < comp_number:
      number_of_attempt -= 1
      print("Too low.")
      play = True
    else:
      print("Yes,You Guessed the number correctly.You won")
      play = False
    
    

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 to 100")
comp_number = random.randint(1,100)
level = input("Choose a difficulty level.Type 'Easy' or 'Hard':").lower()
if level == "easy":
  n_attemp = 10
  game(n_attemp)
elif level == "hard":
  n_attemp = 5
  game(n_attemp)
