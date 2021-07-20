# ROCK PAPER SCISSOR

rock = (""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""")

scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

import random
actions = [rock, paper, scissor]

print("Decide You Hand Move 0-Rock, 1-Paper, 2-Scissor \n")
actions_no = int(input(""))
human_move = actions[actions_no]
print("\n Your Move = ", human_move)

random_no = random.randint(0,2)
comp_move = actions[random_no]
print("\n Computer Move = \n",comp_move)

if(human_move==actions[0]):
    if((human_move==actions[0]) and (comp_move==actions[0])):
        print("Its Draw")
    elif((human_move==actions[0]) and (comp_move==actions[1])):
        print("You Loose")
    elif((human_move==actions[0]) and (comp_move==actions[2])):
        print("You Win")    
        
elif(human_move==actions[1]): 
    if((human_move==actions[1]) and (comp_move==actions[1])):
        print("Its Draw")
    elif((human_move==actions[1]) and (comp_move==actions[0])):
        print("You Win")
    elif((human_move==actions[1]) and (comp_move==actions[2])):
        print("You Loose")
            
elif(human_move==actions[2]):
    if((human_move==actions[2]) and (comp_move==actions[2])):
        print("Its Draw")
    elif((human_move==actions[2]) and (comp_move==actions[0])):
        print("You Loose")
    elif((human_move==actions[2]) and (comp_move==actions[1])):
        print("You Win")
