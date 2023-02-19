import random
import time

# Instructions for normal rock paper scissors
def rps_instructions():
    print()
    print("Instructions for Rock-Paper-Scissors: ")
    print()
    print("Rock crushes Scissors ")
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print()


# Game execution starts here
def rps():

    # Global so that everything in this function has access to the variable
    global rps_table
    global game_map
    global name

    while True:
        print("-------------------------------")
        print("\t\tMenu")
        print("-------------------------------")
        print('Enter "help" for instructions.')
        print('Enter "Rock", "Paper", "Scissors" to play!')
        print('Enter "exit" to quit')
        print("-------------------------------")
        print()

        inp = input("Enter your move: ")

        if inp.lower() == "help":
            rps_instructions()
            continue
            # calls this function to print out instructions
        elif inp.lower() == "exit":
            break
        elif inp.lower() == "rock":
            player_move = "rock"
        elif inp.lower() == "paper":
            player_move = "paper"
        elif inp.lower() == "scissors":
            player_move = "scissors"
        else:
            print("Wrong input!")
            rps_instructions()
            continue

        print("Computer making a move")
        print()
        time.sleep(2)
        # Computer waits 2 seconds before printing out what they did

        comp_move = random.randint(0, 2)
        # Variable that tells computer to choose a random integer between 0 and 2

        print("Computer chooses")

        if comp_move == 0:
            print("rock!")
            comp_move_string = "rock"
        elif comp_move == 1:
            print("paper")
            comp_move_string = "paper"
        else:
            print("scissors")
            comp_move_string = "scissors"

        if comp_move_string == "scissors" and player_move == "scissors":
            print("Its a tie!")
        if comp_move_string == "paper" and player_move == "paper":
            print("Its a tie!")
        if comp_move_string == "rock" and player_move == "rock":
            print("Its a tie!")
        if comp_move_string == "rock" and player_move == "scissors":
            print("Computer wins!")
        if comp_move_string == "rock" and player_move == "paper":
            print("You win!")
        if comp_move_string == "scissors" and player_move == "rock":
            print("You win!")
        if comp_move_string == "scissors" and player_move == "paper":
            print("Computer wins!")
        if comp_move_string == "paper" and player_move == "rock":
            print("Computer wins")
        if comp_move_string == "paper" and player_move == "scissors":
            print("You win")

        print()
        time.sleep(3)


def rpsls():

    while True:
        print("-------------------------------")
        print("\t\tMenu")
        print("-------------------------------")
        print('Enter "help" for instructions.')
        print('Enter "Rock", "Paper", "Scissors", "Lizard", "Spock" to play!')
        print('Enter "exit" to quit')
        print("-------------------------------")
        print()

        inp = input("Enter your move: ")

        if inp.lower() == "help":
            rps_instructions()
            # Call function that prints out instructions
            continue

        elif inp.lower() == "lizard":
            player_move = 3

        elif inp.lower() == "spock":
            player_move = 4

        else:
            print("Wrong input")
            rps_instructions()
            continue
        
rps()