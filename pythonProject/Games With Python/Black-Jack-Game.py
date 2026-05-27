#Day 11 Project
#Black Jack Game

import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#Function to distribure cards to players
def card_distribution():
  card = random.choice(cards)
  return card

#Function to calculate the score
def calculate_score(card):
  score = sum(card)
  if score == 21 and len(card) == 2:
    return 0;
  
  if 11 in card and score>21:
    cards.remove(11)
    cards.append(1)
  return score

#Function to find the winner
def compare(u_score,c_score):
  if u_score > 21 and c_score > 21:
    return "Draw,because you both went over can decide winner or loser"
  
  if u_score == c_score:
    return "Draw"
  elif u_score == 0:
    return "You Won with a BlackJack"
  elif c_score == 0:
    return "Opponent Won with a BlackJack"
  elif u_score > 21:
    return "You went over.You Lose"
  elif c_score > 21:
    return "Opponent went over.You Won"
  elif u_score>c_score:
    return "You Won"
  else:
    return "You Lose"

#Main logic of the game
def game():
  print(logo)
  user_card = []
  computer_card = []
  for _ in range(2):
    user_card.append(card_distribution())
    computer_card.append(card_distribution())
  user_score = calculate_score(user_card)
  computer_score = calculate_score(computer_card)
  print(f"Your cards are {user_card}.Your Total is {user_score}.")
  print(f"Computers first card is {computer_card[0]}")
  should_continue = True
  while should_continue:
    if user_score == 0 or computer_score == 0 or user_score > 21:
      should_continue = False
    else:
      choice = input("Type 'Y' to get another card or 'N' to pass over:").lower()
      if choice == 'y':
        user_card.append(card_distribution())
        user_score = calculate_score(user_card)
        should_continue = False
      else:
        should_continue = False
  while computer_score != 0 and computer_score < 17:
    computer_card.append(card_distribution())
    computer_score = calculate_score(computer_card)
    break
  print(f"Your final hand is:{user_card},final socre:{user_score}")
  print(f"Opponents final hand is:{computer_card},final score:{computer_score}")
  print(compare(user_score,computer_score))

play = True
while play:
  game()
  ch = input("Press Y to play again or press any key to exit").lower()
  if ch == "y":
      print("\n\n\n")
      play = True
  else :
    play = False


  




