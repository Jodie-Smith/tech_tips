import random

def player_option():
    user_choice = input("Choose Rock(r), paper(p) or scissors(s): ").lower()
   
    if user_choice in ["r", "rock"]:
        user_choice = "rock"
   
    if user_choice in ["p", "paper"]:
        user_choice = "paper"
    
    if user_choice in ["s", "scissors"]:
        user_choice = "scissors"
    
    if user_choice not in ["r", "rock", "p", "paper", "s", "scissors"]:
        print("Please enter r, p, or s.")
        user_choice = player_option()

    return user_choice


def computer_option():
    computer_choice = random.randint(0, 2)
   
    if computer_choice == 0:
        computer_choice = "rock"
    
    if computer_choice == 1:
        computer_choice = "paper"
    if computer_choice == 2:
        computer_choice = "scissors"

    return computer_choice



def getWinner():

    
    user_choice = player_option()
    computer_choice = computer_option()
    answer = ""

    if user_choice == "rock":
       
        if computer_choice == "rock":
            answer = "You chose rock, the computer chose rock. It's a tie!"
       
        if computer_choice == "paper":
            answer = "You chose rock, the computer chose paper. You lose."
       
        if computer_choice == "scissors":
            answer = "You chose rock, the computer chose scissors. You win!"


    if user_choice == "paper":
        
        if computer_choice == "rock":
            answer = "You chose paper, the computer chose rock. You win!"
        
        if computer_choice == "paper":
            answer = "You chose paper, the computer chose paper. It's a tie!"
        
        if computer_choice == "scissors":
            answer = "You chose paper, the computer chose scissors. You lose."

    if user_choice == "scissors":
        
        if computer_choice == "rock":
            answer =  "You chose scissors, the computer chose rock. You lose."
        
        if computer_choice == "paper":
            answer = "You chose scissors, the computer chose paper. You win!"
        
        if computer_choice == "scissors":
            answer = "You chose scissors, the computer chose scissors. It's a tie!"

    return answer

def runGame():

    print(getWinner())

    user_choice = input("Do you want to play again? y/n?").lower()
    if user_choice in ['y', 'yes']:
        runGame()
    else:
     print("end of game")


runGame()

