import random

choices = ["rock","paper","scissor"]
computer = random.choice(choices)
user = input("rock,paper or scissor? ").lower()
print(f"Computer chose: {computer}")

if user not in choices:
    print("Invalid!")
elif computer == user:
    print("Draw!")
elif computer == "rock" and user == "paper" :
    print("You Win!")
elif computer == "rock" and user == "scissor" :
    print("You Lose!")
elif computer == "paper" and user == "scissor" :
    print("You Win!")
elif computer == "paper" and user == "rock" :
    print("You Lose!")
elif computer == "scissor" and user == "rock" :
    print("You Win!")
elif computer == "scissor" and user == "paper" :
    print("You Lose!")
print("Lets play Again!!")