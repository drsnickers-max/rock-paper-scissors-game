import random
options=("rock","paper","scissors")
player=0
computer=random.choice(options)
is_running=True
player_score=0
computer_score=0




while is_running:
 player=  input("enter your choice rock,paper,scissors ")
 if player not in options:
   print("enter a valid choice")
   continue
 print(f"player choose {player}")
 computer=random.choice(options)
 print(f"computer choose {computer}")

 if player==computer:
  print("it is a tie")
  continue
 elif player=="rock" and computer=="scissors":
  print("player won")
  player_score+=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  continue
 elif player=="scissors" and computer=="paper":
  print("player won")
  player_score +=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  continue
 elif player=="paper" and computer=="rock":
  print("player won")
  player_score+=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  continue
 elif player=="paper" and computer=="scissors":
  print("computer won")
  computer_score+=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  continue
 elif player=="rock" and computer=="paper":
  print("computer won")
  computer_score+=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  continue
 elif player=="scissors" and computer=="rock":
  print("computer won")
  computer_score+=1
  print(player_score)
  print(computer_score)
  if player_score==5:
   print("player won!!")
   is_running=False
  elif computer_score==5:
    print("computer won ;(")
    is_running=False
  