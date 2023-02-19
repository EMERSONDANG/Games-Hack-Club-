import random as rand  # random pokemon names, variable name is random
import time  # Delays program between pokemon spawns
import sys  # Helps us leave the program once code is done

file = open("allpokemon.txt")
# Create a variable called file which stores the allpokemon.txt file

all_pokemon = file.readlines()
# Splits the file contents on different lines and makes
# them as list elements []. Essentially reads the file and the lines

owned_pokemon = []
# Create list of pokemon we own

while True:
    old_save = input("Do you have a safe file? (y/n)")

    if old_save.lower().strip() == "n":
        print("Welcome!")
        break

    elif old_save.lower().strip() == "y":

        own_file = input("Welcome back! Please type the name of your save file!")

        try:
            own_file_start = open(own_file, "r")
            own_file_start.readlines

            for i in own_file_start:
                i.strip()

            own_file_start.close()
            print("All set!")
            break

        except FileNotFoundError:
            print("There was a problem finding your save file. Please try again.")

    else:
        print("Please enter the letter n for no or the letter y for yes!")

while True:

    print("Waiting for a new pokemon...")
    time.sleep(rand.randint(5, 10))

    print("A pokemon has appeared! ")
    current_pokemon = rand.choice(all_pokemon).strip().upper()
    # random.choice chooses a random pokemon name from the file
    # allpokemon.txt, strip() removes any potential white space (space bars)
    # read within the file, upper() causes the pokemon's name to show up in # all upper case letters
    print("It's a " + current_pokemon + "!")

    catches_left = 3
    # Amount of poke balls user has. 3 tries

    while True:
        catch_state = input("Would you like to catch it? ")
        # Asks user for input, yes or no

        if catch_state.lower() == "y" or catch_state.lower() == "yes":
            if catches_left <= 0:
                print(
                    "You did not catch the "
                    + current_pokemon
                    + " as you have no more poke balls. "
                )
                break

            # Takes user input and converts all letters to lowercase
            else:
                catch = rand.randint(1, 100)
                # Means random.randomint, create a random integer between 1-100

                if catch <= 33:
                    owned_pokemon.append(current_pokemon)
                    # Append function adds the current all_pokemon into the list

                    if current_pokemon not in owned_pokemon:
                        print(
                            current_pokemon
                            + " added to the Pokedex since it was new ! "
                        )

                    print("You have caught the " + current_pokemon + "!")
                    break

                else:
                    catches_left = catches_left - 1
                    print("The " + current_pokemon + " popped out! Try again! ")

        elif catch_state.lower() == "n" or catch_state.lower() == "no":
            print("Bye " + current_pokemon + "!")
            break

        else:
            print("Please enter either yes, no, y or n! ")

    print("What would you like to do? ")
    print("O = Check owned pokemon ")
    print("P = Check current Pokedex ")
    print("U = Update the pokedex and owned pokemon ")
    print("N = Exit ")
    print("S = Exit program")

    while True:
        choice = input("Pick your choice!")

        if choice.lower() == "o":
            print(owned_pokemon)

        if choice.lower() == "p":
            print(set(owned_pokemon))

        if choice.lower() == "u":
            print("Working on it!")
            # create file
            owned_pokemon_file = open("owned_pokemon.txt", "w")

            # for every caught pokemon
            for i in owned_pokemon:
                # write it to a file and split pokemon with new lines
                owned_pokemon_file.write(i + "\n")
            # close to save
            owned_pokemon_file.close()

            # same for pokedex
            pokedex_file = open("pokedex.txt", "w")
            for i in set(owned_pokemon):
                pokedex_file.write(i + "\n")
            pokedex_file.close()

            print("\nDone! View them in your explorer tab.")

        if choice.lower() == "n":
            break

        if choice.lower() == "s":
            sys.exit()
