"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""


import random
list_item =["Rock","Paper","Scissore"]

Human = input('Enter your choice = Rock,Paper,Scissore = ')
Computer = random.choice(list_item)
print(f"Human Choice = {Human} and Computer Choice = {Computer}")

if Human == Computer:
    print("Both chooses same: = Match Tie")

elif Human == "Rock":
    if Computer == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You win")

elif Human == "Paper":
    if Computer == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You win")

elif Human == "Scissor":
    if Computer == "Paper":
        print("Scissor cuts paper, You win")
    else:
        print("Rock smashes scissor, Computer win")
