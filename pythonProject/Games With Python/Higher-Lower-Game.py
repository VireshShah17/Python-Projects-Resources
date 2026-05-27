from art import logo
from art import vs
from gamedata import data
import random

print(logo)

#Function to print data in formated way
def format_data(account):
  account_name = account['name']
  account_desc = account['description']
  account_count = account['country']
  return f"{account_name},a {account_desc},from {account_count}"

#Function to check the followers
def check_follower(guess,f_account,s_account):
  if guess == "a":
    if f_account > s_account:
      return True
    else:
      return False
  else:
    if s_account > f_account:
      return True
    else:
      return False



first = random.choice(data)
second = random.choice(data)
while first == second:
    second = random.choice(data)
print(f"Compare A:{format_data(first)}")
print(vs)
print(f"Against B:{format_data(second)}")
user_guess = input("Who has more follower?Type 'A' or 'B'").lower()
first_follower_count = first['follower_count']
second_follower_count = second['follower_count']
is_correct = check_follower(user_guess,first_follower_count,second_follower_count)
score = 0 
while is_correct == True:
  print("You are Right")
  print("\n\n\n")
  score += 1
  print(f"Your score is {score}")
  first = second
  second = random.choice(data)
  while first == second:
    second = random.choice(data)
  print(f"Compare A:{format_data(first)}")
  print(vs)
  print(f"Against B:{format_data(second)}")
  user_guess = input("Who has more follower?Type 'A' or 'B'").lower()
  first_follower_count = first['follower_count']
  second_follower_count = second['follower_count']
  is_correct = check_follower(user_guess,first_follower_count,second_follower_count)
  if is_correct == False:
    break
print("Sorry you are Wrong")
print(f"Your finale score is {score}.")



  
  
