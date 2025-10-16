import random

# Rock Paper Scissors Game
# ------------------------
# Rules:
# 1 for Rock
# 0 for Paper
# -1 for Scissors

# Computer randomly picks one of rock, paper, or scissors
c = random.choice([1, 0, -1])

# Ask user for their choice
u = input("Enter your choice (r for rock, p for paper, s for scissors): ")

# Mapping user input to numeric values
udict = {"r": 1, "p": 0, "s": -1}

# Mapping numeric values to readable names
rdict = {1: "rock", 0: "paper", -1: "scissor"}

# Convert user input to numeric value
k = udict[u]

# Show both choices
print(f"Your pick: {rdict[k]}")
print(f"Computer's pick: {rdict[c]}")

# Determine the result
if c == k:
    print("It's a draw")
else: 
    if c == 1 and k == 0:
        print("You win")
    elif c == 1 and k == -1:
        print("You lose")
    elif c == 0 and k == 1:
        print("You lose")  
    elif c == 0 and k == -1:
        print("You win") 
    elif c == -1 and k == 1:
        print("You win")
    elif c == -1 and k == 0:
        print("You lose")
    else:
        print("Something went wrong")
git init
git add .
git commit -m "mini-project-1" 
git branch -M main
git remote add origin https://github.com/<mohdtusi>/MiniProject1.git 
git push -u origin main