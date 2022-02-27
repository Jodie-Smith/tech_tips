import random

def player_option():
   user_choice = input("Choose Rock(r), paper(p) or scissors(s): ").lower()
   match user_choice:
        case "r" | "rock":
            user_choice = "rock"
        case "p" | "paper":
            user_choice = "paper"        
        case "s" | "scissors":
            user_choice = "scissors"
        case _:
            print("Please enter r, p, or s.")
            user_choice = player_option()

   return user_choice


def computer_option():
    computer_choice = random.randint(0, 2)
    match computer_choice:
        case 0:
            computer_choice = "rock"
        case 1:
            computer_choice = "paper"
        case 2:
            computer_choice = "scissors"

    return computer_choice



def getWinner():
    user_choice = player_option()
    computer_choice = computer_option()
    answer = ""

    if user_choice == computer_choice:
            answer = "It's a tie!"
    else:
        match user_choice:
            case "rock":
                if computer_choice == "scissors":
                    answer = "You win!"
                if computer_choice == "paper":
                    answer = "You lose."
            case "paper":
                if computer_choice == "rock":
                    answer = "You win!"
                if computer_choice == "scissors":
                    answer = "You lose."
            case "scissors":
                if computer_choice == "paper":
                    answer = "You win!"
                if computer_choice == "rock":
                    answer =  "You lose."
            case computer_choice:
                answer = "It's a tie!"

    return f"You chose {user_choice}, the computer chose {computer_choice}. {answer}"

def runGame():

    print(getWinner())

    user_choice = input("Do you want to play again? y/n?").lower()
    if user_choice in ['y', 'yes']:
        runGame()
    else:
     print("end of game")


runGame()

