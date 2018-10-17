'''
a rock,paper,scissor game. choose either of those words to play.
'''
from random import randint
l = ["ROCK", "PAPER", "SCISSORS"]
result = {"tie":"Yawn It's a tie!","won":"Yay you won!","lost":"Aww you lost!"}

def decide_winner(user_choice, computer_choice):
  computer_choice = l[computer_choice]
  print("User: %s" % (user_choice))
  print("CPU: %s" % (computer_choice))
  print("*"*30)
  if user_choice == computer_choice:
    print(result["tie"])
  elif (user_choice == l[0] and computer_choice == l[2]) or (user_choice == l[1] and computer_choice == l[0]) or (user_choice == l[2] and computer_choice == l[1]) :
    print(result["won"])
  else:
    print(result["lost"])
  print("*" * 30)
  
def play_RPS():
  user_choice = input("Enter Rock, Paper or Scissors: ").upper()
  computer_choice = randint(0,2)
  decide_winner(user_choice, computer_choice)
  
play_RPS()  