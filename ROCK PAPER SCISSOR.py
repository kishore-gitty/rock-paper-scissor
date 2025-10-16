import random
import time
print("shall we begin the rock paper scissor game")
times=int(input("HOW MANY MATCH YOU NEED TO PLAY:"))
for i in range(times):
    def choices():
        print("rock")
        print("paper")
        print("scissor")
    count = 0
    options = ['rock','scissor','paper']
    player = None
    computer = random.choice(options)
    player = input("enter a choice:")
    while player not in options:
        print("enter the correct choice..")
        print(f"here the {player} doesn't exist in the game")
        print("the choices are..")
        choices()
        player = input("enter a choice:")
        if player in options:
            break
        else:
            continue
    print(f"you : {player}")
    print(f"computer : {computer}")
    if computer == player:
        print("match draw!!")
        count = 0
    elif player == "rock" and computer == "paper":
        print("computer wins!! \n you lost!!")
        count = 0
    elif player == "rock" and computer == "scissor":
        print("computer lost!! \n you wins!!")
        count +=1
    elif player == "paper" and computer == "rock":
        print("computer lost!! \n you wins!!")
        count +=1
    elif player == "scissor" and computer == "paper":
        print("computer lost!! \n you wins!!")
        count +=1
    elif player == "paper" and computer == "scissor":
        print("computer wins!! \n you lost!!")
        count = 0
    elif player == "scissor" and computer == "rock":
        print("computer wins!! \n you lost!!")
        count = 0
print(f"congratulations you had won {count} times out of {times} times!!")
    
    










