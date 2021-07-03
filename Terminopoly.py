from hashlib import new
import random
import pickle
# Level One & Two blehata020 code implemented. Level Three mngwenya020 code implemented


class Game:  # Set the class that will house the functions

    def Dice_Roll(self):  # Level 1 - Dice : This functions purpose is to roll a dice
        # Generates a random number between 1 and 6
        self.roll = random.randint(1, 6)

        if self.roll == 6:  # If the player rolls a 6 this allows them to roll again
            print("You rolled a 6 , Get another turn.")

            play.Players_Choice()

        else:
            print("You rolled a " + str(self.roll))

    def Players_Choice(self):
        self.choice = str(
            input("Would you like to roll the dice? Yes Or No: "))  # This function asks if the player would like to roll the dice

        if self.choice == "Yes":
            play.Dice_Roll()  # Calls for the dice to be rolled
            play.board_position()  # Calls the board position function
        else:
            pass

    # This function will deterimine how many places to move on the board
    def board_position(self):
        if self.roll == 6:
            return 6  # if the player rolls a 6 it will return a 6 before continueing

        position = start_position  # the functions variable position which can be changed is set to the global variable start_position which cant be changed at the this point

        position = position + self.roll
        if position > 16:
            position = position - 16
            return position
        else:
            pass
        return position


Locations = {1: "Begin", 2: "Python Hotel", 3: "Community Chest", 4: "OOP-sy B&B", 5: "Jail", 6: "CSS Heights", 7: "Chance", 8: "JS Inn", 9: "Free Parking",
             10: "Memory Space", 11: "Community Chest", 12: "Ram House", 13: "Straight To Jail", 14: "Cache de Cookie", 15: "Chance", 16: "ROM-ance Inn"}
# All the locations for the game are stored within a Dictionary via Index and Place. Referenced from https://stackoverflow.com/questions/45072283/how-to-use-a-python-dictionary
# Level 2 - creating locations

WTC_wallet = 500
number_of_moves = 0
total = 0
property_holdings = []
start_position = 1
# global variables are created
# Level 1

user_input = str(
    input("Would you like to play some Terminopoly? Enter 'Yes' to play: "))
# Yes will begin the code

load_game = str(input("Would you like to load a game? Yes Or No: "))

if load_game == "Yes":
    # Level 3 - load
    property_holdings = pickle.load(open("properties.dat", "rb"))
    WTC_wallet = pickle.load(open("WTCWallet.dat", "rb"))
    new_position = pickle.load(open("place.dat", "rb"))
    number_of_moves = pickle.load(open("moves.dat", "rb"))
    # Using pickle this loads the data from the binary files from the drive and sets it to the variable
    print("Your current properties owned: ")
    print(property_holdings)
    print("Your balance is W" + str(WTC_wallet))
    print("You've played " + str(number_of_moves) +
          " moves. And your current location is " + Locations[new_position])
    # Lets the user know their saved info


else:
    print("A new game has begun! ")

play = Game()  # The game class is set to play variable in order to be called

while user_input != "No":  # As long as the user input is no the loop will continue

    play.Players_Choice()  # Calls the function that asks for the players input
    # sets the players position after rolling the dice to the return value of board_position function
    new_position = play.board_position()
    # calls the board posistion function from the game class and sets that return value to new position

    if new_position == 1:
        print("You pass go collect WTC 200")
        WTC_wallet = WTC_wallet + 200
        print("Youre new balance is WTC" + str(WTC_wallet))
        # If the players position lands on 1 the players get WTC 200

    elif new_position == 3 or new_position == 11:
        # Level 2 - Community Chest
        # If a players positions is either 3 or 11 the community chest elif statement is run

        print("You have landed on Community Chest.")
        # Randomly picks a card for the player
        card_selector = random.randint(1, 2)

        if card_selector == 1:
            start_position = 1
            print("You picked up 'Advance to Go' and collect WTC 200 ")
            WTC_wallet = WTC_wallet + 200
            print("New Balance is WTC" + str(WTC_wallet))

        elif card_selector == 2:
            print("You picked up 'Bank error in yout favor' receive WTC 250 ")
            WTC_wallet = WTC_wallet + 250
            print("New balance WTC" + str(WTC_wallet))

    elif new_position == 7 or new_position == 15:  # Landed on the chance card
        # Level 2 - Chance

        print("You have landed on Chance ")
        card_selector = random.randint(1, 2)

        if card_selector == 1:
            # Calls item number 12 in the Locations Dictionary
            print("Advance to " + Locations[12])

            if new_position == 7:  # checks wheter they will pass go or not when their position is changed
                start_position = 12  # If they are at 7 the move to 12 without collecting 200 WTC

            else:  # Means they are at the other chance location and will pass go and collect WTC 200
                print("You passed Go collect WTC 200")
                WTC_wallet = WTC_wallet + 200
                start_position = 12
                print("New balance is WTC" + str(WTC_wallet))

        elif card_selector == 2:
            print("You have a telephone fine.")
            WTC_wallet = WTC_wallet - 50
            print("New balance is WTC" + str(WTC_wallet))

    elif new_position == 9:
        print("You've landing on Free parking")

    elif new_position == 5:
        print("You've landed on Jail , Just visiting. Luckily")
# Level 1 - Jail System
    elif new_position == 13:  # Sends player to Jail
        print("Youve landed on Straight To Jail, Pass go and do not collect 200")

        jail_decision = str(input(
            "To exit Jail roll the dice three times Or Pay a Fine? Enter 'Roll' or 'Fine' to continue: "))  # Asks the user wheter they want to roll or pay a fine

        while jail_decision == "Roll":  # This section of code rolls a dice three times to see if a player can score above 10
            print("You need to roll a 10 or higher to exit")

            while total < 9 and jail_decision == "Roll":  # These two conditions must be true to keep player in the loop
                total = 0  # A variable only use in this conditional statement so its sets to zero every loop
                for i in range(1, 3):
                    roll = random.randint(1, 6)
                    total = roll + total
                    print("you rolled a " + str(roll))
                print("Your toal was " + str(total))

                if total < 10:  # If there roll was unsuccessful asks user wheter they would like to change their mind continuing to the next statement or leaving them in the while loop
                    jail_decision = str(
                        input("Would you like to try again or pay a fine? Enter 'Roll' or 'Fine'"))
                else:

                    print("Youve rolled a " + str(total) + " you may leave Jail")
                    # IF above 10 sets the decision variable to an empty string exiting the loop
                    jail_decision = ""

                if jail_decision == "Fine":  # If player first tried to roll the dice but then decided to pay the fine this statement is run

                    if WTC_wallet > 150:  # If they are able to afford 150 is dectucted from the users wallet and jail decision is set to an empty string exiting the while loop
                        print("You paid a WTC 150 fine and left Jail")
                        jail_decision = ""
                        WTC_wallet = WTC_wallet - 150
                        print("Youre new balance is W"+str(WTC_wallet))
                    else:
                        print(
                            "You cant afford to leave jail , your only exit is to roll the dice. ")
                        # if they unable to afford the fine jail decision is set back to roll in order to keep them within the while loop
                        jail_decision == "Roll"
                else:
                    pass

            # Adds a move count at the end of the loop for as long as the jail decision variable is Roll
            number_of_moves = number_of_moves + 1

        while jail_decision == "Fine":  # If the user initially chooses to pay the fine this loop is implemented

            if WTC_wallet > 150:  # CHecks if they are able to pay the fine
                print("You paid a WTC 150 fine and left Jail")
                jail_decision = ""
                WTC_wallet = WTC_wallet - 150
                print("Your new balance is W" + str(WTC_wallet))

            else:  # If the user cannot afford the fine a similar while loop to the initial while == Roll loop is implemented
                print(
                    "You cant afford to leave jail , your only exit is to roll the dice. ")
                jail_decision == "Roll"

                while jail_decision == "Roll":  # This loop has no option to pay a way out the user has to stay until they roll a 10

                    print("You need to roll a 10 or higher to exit")

                    while total < 9 and jail_decision == "Roll":

                        total = 0
                        for i in range(1, 3):

                            roll = random.randint(1, 6)
                            total = roll + total
                            print("you rolled a " + str(roll))

                        if total < 9:

                            print("You rolled a " + str(total) + "Roll again")
                        else:
                            print("Youve rolled a " + str(total) +
                                  " you may leave Jail")
                            jail_decision = ""
                    number_of_moves = number_of_moves + 1

    else:
        # Udes the dictionary to let user know where they have landed
        print("You've landed on " + Locations[new_position])
        # prints the list that holds all the users properties
        print("Current Property Holdings: " + str(property_holdings))
        # Gets the length of the list
        amount_of_properties = len(property_holdings)
        # set a string variable to a location from the locations dictionary according to the new position variable as a index
        property_landed_on = Locations[new_position]

        # Checks if player owns property if yes pays them out rent
        # A for loop that will run for the length of the properties owned
        for i in range(amount_of_properties):

            if property_landed_on == property_holdings[i]:
                print("You own this building, here is your money collect from rent ")
                # Calculates how much to pay out based on new position
                WTC_wallet = WTC_wallet + (5 * new_position)
                print("New balance is " + str(WTC_wallet))
            else:
                pass

        purchase_order = str(
            input("Would you like to purchase " + Locations[new_position] + "? Yes or No: "))  # Plays code that gives user the option to buy the property

        if purchase_order == "Yes":

            if new_position < 5:  # determimes what street the user is on
                confirmation = str(input(
                    "Houses on Java Street cost WTC 100. Your current balance is " + str(WTC_wallet) + ". Are you sure? "))

                if confirmation == "Yes":
                    if WTC_wallet >= 100:  # Checks wether they can afford the place
                        # adds the property the user has purchased to the property holdings list
                        property_holdings.append(Locations[new_position])
                        WTC_wallet = WTC_wallet - 100  # subtracts the cost of the place
                        print("You are the new owner of  " +
                              Locations[new_position]+". Your new wallet balance is " + str(WTC_wallet))
                    else:
                        print(
                            "You cannot affort this property, your balance " + str(WTC_wallet))
                else:
                    print("Alright maybe next time.")

            elif new_position > 5 and new_position < 10:
                confirmation = str(input(
                    "Houses on HTML DOM Lane cost WTC 200. Your current balance is " + str(WTC_wallet) + ". Are you sure? "))
                if confirmation == "Yes":
                    if WTC_wallet >= 200:
                        property_holdings.append(Locations[new_position])
                        WTC_wallet = WTC_wallet - 200
                        print("You are the new owner of  " +
                              Locations[new_position]+". Your new wallet balance is " + str(WTC_wallet))
                    else:
                        print(
                            "You cannot affort this property, your balance " + str(WTC_wallet))
                else:
                    print("Alright maybe next time.")

            elif new_position > 9 and new_position < 14:
                confirmation = str(input(
                    "Houses on Assembly cost WTC 300. Your current balance is " + str(WTC_wallet) + ". Are you sure? "))
                if confirmation == "Yes":
                    if WTC_wallet >= 300:
                        property_holdings.append(Locations[new_position])
                        WTC_wallet = WTC_wallet - 300
                        print("You are the new owner of  " +
                              Locations[new_position]+". Your new wallet balance is " + str(WTC_wallet))
                    else:
                        print(
                            "You cannot affort this property, your balance " + str(WTC_wallet))
                else:
                    print("Alright maybe next time.")

            elif new_position > 13 and new_position <= 16:
                confirmation = str(input(
                    "Houses in CPU City cost WTC 400. Your current balance is " + str(WTC_wallet) + ". Are you sure? "))
                if confirmation == "Yes":
                    if WTC_wallet >= 400:
                        property_holdings.append(Locations[new_position])
                        WTC_wallet = WTC_wallet - 400
                        print("You are the new owner of  " +
                              Locations[new_position]+". Your new wallet balance is " + str(WTC_wallet))
                    else:
                        print(
                            "You cannot affort this property, your balance " + str(WTC_wallet))
                else:
                    print("Alright maybe next time.")
        else:
            pass

    start_position = new_position  # changes the star position variable in order to be used in the board position function. These two variable are used in a loop and the position variable acting as ROM
    number_of_moves = number_of_moves + 1
    # To determine whether to start the overall while loop again or exit
    user_input = str(input("Would you like to continue playing? Yes or No: "))
# Once the exit the while loop there results is printed out

print("Your final balance is W" + str(WTC_wallet) +
      "You acheived this in " + str(number_of_moves) + " moves.")

# Gives player option to save the game
save_game = str(input("Would you like to save this game? Yes Or No: "))

if save_game == "Yes":
    # Level 3 - save

    # Saves the variables as a binary file to the drive
    pickle.dump(property_holdings, open("properties.dat", "wb"))
    pickle.dump(WTC_wallet, open("WTCWallet.dat", "wb"))
    pickle.dump(new_position, open("place.dat", "wb"))
    pickle.dump(number_of_moves, open("moves.dat", "wb"))
    print("Your data has been saved.")


else:
    print("Alright, thank you for playing.")
