#Day 4 Project
#Rock Paper scissor game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
u_choice = int(input("What do you choose?Type 0 for rock,1 for paper and 2 for scissor:"))
print("Users choice:")
if u_choice == 0:
    print(rock)
elif u_choice == 1:
    print(paper)
elif u_choice == 2:
    print(scissors)
else:
    print("Wrong Choice entered.")
lst=[0,1,2]
c_choice=random.choice(lst)
print("Computers choice:")
if c_choice == 0:
    print(rock)
elif c_choice == 1:
    print(paper)
elif c_choice == 2:
    print(scissors)

if u_choice==0:
  if c_choice==0:
    print("Draw!")
  elif c_choice==1:
    print("You Lose!")
  elif c_choice==2:
    print("You Win!")

elif u_choice==1:
  if c_choice==0:
    print("You Won!")
  elif c_choice==1:
    print("Draw!")
  elif c_choice==2:
    print("You Lose!")


elif u_choice==2:
  if c_choice==0:
    print("You Lose!")
  elif c_choice==1:
    print("You Win!")
  elif c_choice==2:
    print("Draw!")