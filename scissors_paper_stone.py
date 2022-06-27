import random
import time

Scissors = 1
Paper = 2
Stone = 3

round_number = 0
computer1_weapon = 0
computer2_weapon = 0
computer1_score = 0
computer2_score = 0
count = 0


print("welcome to the game of Scissors,Paper,Stone")
print("")
while count <3:
  count = count + 1
  print("Round:",count)
  computer1_weapon = random.randint(1,3)
  computer2_weapon = random.randint(1,3)
  print(computer1_weapon)
  print(computer2_weapon)
  if computer1_weapon == computer2_weapon:
    print("its a tie")
    computer1_score = computer1_score + 0
    computer2_score = computer2_score + 0
  elif computer1_weapon == 1 and computer2_weapon == 2:
    print("computer1 wins")
    computer1_score = computer1_score + 1
  elif computer1_weapon == 2 and computer2_weapon == 3:
    print("computer1 wins")
    computer1_score = computer1_score + 1
  elif computer1_weapon == 3 and computer2_weapon == 1:
    print("computer1 wins")
    computer1_score = computer1_score + 1
  else:
    print("computer2 wins")
    computer2_score = computer2_score + 1
  print("computer1:",computer1_score,"computer2:",computer2_score)
 
  time.sleep(1)
  print("")
if computer1_score > computer2_score:
    print("computer1 has won")
if computer2_score > computer1_score:
    print("computer2 has won")
elif computer1_score == computer2_score:
    print("its a tie")
print("computer1:",computer1_score)
print("computer2:",computer2_score)
