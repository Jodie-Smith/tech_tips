import random

rock = 0
paper = 1
scissors = 2


def player_option():
    user_choice = input("Choose Rock(r), paper(p) or scissors(s): ").lower()
    if user_choice in ["r", "rock"]:
        user_choice = "rock"
    elif user_choice in ["p", "paper"]:
        user_choice = "paper"
    elif user_choice in ["s", "scissors"]:
        user_choice = "scissors"
    else:
        print("Please enter r, p, or s.")
        player_option()
    return user_choice
#need to correct return when player does not enter correct value


def computer_option():
    computer_choice = random.randint(0, 3)
    if computer_choice == 0:
        computer_choice = "rock"
    elif computer_choice == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
    return computer_choice




user_choice = player_option()
computer_choice = computer_option()

if user_choice == "rock":
    if computer_choice == "rock":
         print("You chose rock, the computer chose rock. It's a tie!")
    elif computer_choice == "paper":
        print("You chose rock, the computer chose paper. You lose.")
    elif computer_choice == "scissors":
        print("You chose rock, the computer chose scissors. You win!")


elif user_choice == "paper":
    if computer_choice == "rock":
         print("You chose paper, the computer chose rock. You win!")
    elif computer_choice == "paper":
        print("You chose paper, the computer chose paper. It's a tie!")
    elif computer_choice == "scissors":
        print("You chose paper, the computer chose scissors. You lose.")

elif user_choice == "scissors":
    if computer_choice == "rock":
        print("You chose scissors, the computer chose rock. You lose.")
    elif computer_choice == "paper":
        print("You chose scissors, the computer chose paper. You win!")
    elif computer_choice == "scissors":
        print("You chose scissors, the computer chose scissors. It's a tie!")



# user_choice = input("Do you want to play again? y/n?").lower()
# if user_choice in ['y', 'yes']:
#     pass
# else:
#     print("end of game")
#