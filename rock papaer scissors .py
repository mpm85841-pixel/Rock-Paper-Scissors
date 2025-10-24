import random

print("Welcome to rock paper scissors game!")

op = ("rock", "paper", "scissors")
player = None

while player not in op:
    player = input("Enter your choice (rock, paper, scissors): ").lower()

computer = random.choice(op)

print(f"player: {player}")
print(f"computer: {computer}")

if player == computer:
    print("TIE!")
elif player == "paper" and computer == "scissors":
    print("LOST!")
elif player == "rock" and computer == "paper":
    print("LOST!")
elif player == "scissors" and computer == "rock":
    print("LOST!")
else:
    print("YOU WON!")