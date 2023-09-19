import random
print("Welcome to the rock/paper/scissors game!")
name=input("Enter your name:")
user_turn=input("Write what would you like to use(rock/paper/scissors):")
computer_turn=["rock","paper","scissors"]
computer_turn=random.choice(computer_turn)
print(f"{name} turn is {user_turn}")
print(f"The computer turn is {computer_turn}")
print(30*"-")
if computer_turn=="rock" and user_turn=="rock":
    print("No one wins!\nThere is a tie!")

elif computer_turn=="paper" and user_turn=="paper":
    print("No one wins!\nThere is a tie!")
    
elif computer_turn=="scissors" and user_turn=="scissors":
    print("No one wins!\nThere is a tie!")
   
if computer_turn=="rock" and user_turn=="paper":
    print(f"{name} you win the game!\nThe paper beats the rock.")

elif computer_turn=="paper" and user_turn=="scissors":
    print(f"{name} you win the game!\The scissors cut the paper.")

elif computer_turn=="scissors" and user_turn=="rock":
    print(f"{name} you win the game!\nThe rock smashes the scissors.")

if computer_turn=="rock" and user_turn=="scissors":
    print(f"Sorry,{name} you lose the game!The rock smashes the scissors.")

elif computer_turn=="paper" and user_turn=="rock":
    print(f"Sorry {name} you lost the game!\nThe paper beats the rock.")

elif computer_turn=="scissors" and user_turn=="paper":
    print(f"Sorry {name} you lost the game!\nThe scissors cut the paper.")

