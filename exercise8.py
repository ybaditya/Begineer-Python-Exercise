#Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

def paper_rock_scissor():
    player_one = input("Player One : Please Input (Rock, Scissors, Paper) : ")
    player_two = input("Player Two : Please Input (Rock, Scissors, Paper) : ")
    if player_one == player_two :
        print("It's Tie")
    elif player_one == "Rock" and player_two =="Scissors":
        print("Player One Win")
    elif player_one == "Rock" and player_two =="Paper":
        print("Player Two Win")
    elif player_one == "Scissors" and player_two =="Paper":
        print("Player One Win")
    elif player_one == "Scissors" and player_two =="Rock":
        print("Player Two Win")
    elif player_one == "Paper" and player_two =="Scissors":
        print("Player Two Win")
    elif player_one == "Paper" and player_two =="Rock":
        print("Player One Win")
    else:
        print("Wrong Format")

paper_rock_scissor()

play_again = input("Do You Want to Play Again (Y/N): ")

while play_again == "Y":
    paper_rock_scissor()
    play_again = input("Do You Want to Play Again (Y/N): ")
    if play_again == "N":
        break






