import random

name = input("Enter your name: ")
print(f"Hello, {name}")

names = {}
score = 0
with open("rating.txt") as f:
    for line in f:
        (k, v) = line.split()
        names[k] = int(v)

user_option = input()

if user_option == "":
    options = ["rock", "paper", "scissors"]
else:
    options = user_option.split(",")

print("Okay, let's start")

while True:
    computer = random.choice(options)
    player = input()

    if player == "!rating":
        if name in names:
            score = names[name]
        else:
            names[name] = 0
        print(f"Your rating: {score}")
        continue

    if player == "!exit":
        print("Bye!")
        break

    if player not in options:
        print("Invalid input")
        continue

    answer_index = options.index(player)
    new_list = options[answer_index + 1:] + options[0:answer_index]

    if computer == player:
        print(f"There is a draw ({computer})")
        names[name] += 50
    elif new_list.index(computer) < len(new_list) // 2:
        print(f"Sorry, but the computer chose {computer}")
    else:
        print(f"Well done. The computer chose {computer} and failed")
        names[name] += 100
