'''
Libby Baker
MCON 141
Assignment: Esacpe the Museum

This a game that requires the user to solve
a series of puzzles in order to exit the program.
The program uses functions to run different puzzles
and lists and accumulators to track the user's progress.
'''


# This function print the menu options
def show_menu(name, energy, clues):
    print()
    print("==========================")
    print(" THE GREAT MUSEUM MYSTERY ")
    print("==========================")
    print()
    print(f"Energy: {energy}")
    print(f"Clues collected: {len(clues)} out of 3")
    print()
    print("1. Enter Gallery 1")
    print("2. Enter Gallery 2")
    print("3. Enetr Gallery 3")
    print("4. View collected clues")
    print("5. Attempt to escape")
    print("6. Quit the museum")
    print()

# This unction operates gallery 1
# It tests whether the user has already completed gallery 1
# If not, it asks the user for an input based on certain criteria
# If the user enters the correct answer, they get a clue
# If the user answers incorrectly, points are deducted
# If the user enters the wrong type of data, they are reprompted
def gallery_one(clues, energy):
    solved = solved_gallery(clues, "Copper 3") # Testing to ensure that the gallery has not been solved yet
    print()
    if solved == 1:
        print("You've already solved Gallery 1")
    else:
        print("ANCIENT NUMBERS ROOM")
        print("I am divisible by 3 and 5, and I am between 20 and 40")
        print("What number am I?")
        print()
        while True:
            answer = input("Your answer:")
            print()
            try: # Ensure that the answer is an integer
                answer = int(answer)
            except ValueError:
                print("Invalid input. Enter a non-negetive whole number; no energy lost")
            else:
                if answer == 30: # If answer was correct
                    print("Correct! You earned the clue: Copper 3")
                    clues.append("Copper 3") # add copper to the list of lues
                else: # If the answer was wrong, reduce energy by 1
                    energy = reduce_energy(energy, 1)
                break
    return energy


# This unction operates gallery 2
# There are many possible answers to this function
# The numeric values of the letters of the words must add up to 100
# Function checks the letters against a list of the letters of the alphabet
# An index of the list of the alphabet gives the numeric value

def gallery_two(clues, energy):
    solved = solved_gallery(clues, "Gold 6")
    print()
    if solved == 1:
        print("You've already solved Gallery 2")
    else:
        print("DOLLAR WORD")
        print("If a is ¢1, and b is ¢2 ")
        print("If c is ¢3, and z is ¢26")
        print("If joy is ¢50, and depression is $1.24")
        print("Come up with a word that is worth exactly a dollar")
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] #List of alphabet letters, these are the only letters that can successfully be entered
        print()
        word_val = 0 # set accumulator for the value of the word
        while word_val == 0: # Sentinel loop will reprompt if the input has invalid characters
          word = input("Enter your word:")
          print()
          for l in word.strip().lower(): #take each letter of the word
              if l in alphabet:# This is the validation. The following loop only runs when the character is in the alphabet
                for index, value in enumerate(alphabet, start=1): # To get the value of each letter, Go through the alphabet to find its index position. The index starts at 1, so that a = 1
                  if l == value: # When the letter matches with a letter in the alphabet
                      word_val += index # add its value (index position) to the word value total
                  else:
                      continue
              else: # If an invalid character was detected
                print("Please enter a real word") # print a message
                print()
                word_val = 0 # reset word value to 0 to make the while loop run again and reprompt
                break # break the middle loop that was running through the letters of the word.
        word_form = word_val/100 # devided the word value by 100 so that it can be formatted like a dollar amount
        print(f"{word} = ${word_form:.2f}") # Prints the dollar amount with two decimal spaces
        if word_val == 100: # If the user enterd a word that amounted to 100
            print(f"Correct! {word} is a dollar word! You've earned a clue: Gold 6") # They get the clue
            print()
            clues.append("Gold 6") # add the clue to the list
        else:
            energy = reduce_energy(energy, 1)# Otherwise, they lose energy
    return energy


# This function operates gallery 3
# It tests whether the user has already completed gallery 3
# If not, it asks the user for an input based on a logic question
# If the user enters the correct answer, they get a clue
# If the user answers incorrectly, points are deducted
# If the user enters the wrong type of data, they are reprompted
def gallery_three(clues, energy):
    solved = solved_gallery(clues, "Silver 1") # test to see if the clue is already one the clue list, meaning that the puzzle was already solved
    print()
    if solved == 1:
        print("You've already solved Gallery 3")
    else:
        print("LOGIC CHAMBER")
        print("THE door opens when both lamps are on OR the master key is inserted.")
        print("Lamp A off; Lamp B on; Master key: inserted")
        print("Does the door open? Enter 1 for yes, 0 for no")
        print()
        while True:
            answer = input("Your answer: ")
            print()
            try:
              answer = int(answer) # insuring that the input is an integer
              if answer != 1 and answer != 0: # If the user gave neither acceptable answer
                  print("Invalid input. Please enter 1 or 0.")
                  continue # reprompt
            except ValueError: # unless the input was not an integer
              print("Invalid input, please enter 1 or 0")
            else: # If the input was valid
                break # end validation loop
        if answer == 1: # Check for the right answer
            print("Correct! You've earned aclue: Silver 1")
            clues.append("Silver 1")
        else:
            energy = reduce_energy(energy, 1)
    return energy

# This function reduces the user's energy
# It runs whenever a player enters and incorrect input
# It passes in the variable energy and returns the new, reduced energy
def reduce_energy(energy, cost=1): # takes the parameter ( and arguement) energy, manipulates it, and returns it
    new_energy = energy - cost # subtract 1 from the current energy
    print(f"Incorrect answer. Energy remaining: {new_energy}")
    print()
    return new_energy # return new energy

# This function is used to test whether the user solved a particualr puzzle
# If that puzzle's clue was already added to the clue list
# it returns that the puzzle has already been solved
def solved_gallery(clues, clue):
  if clue in clues: # If the clue was already added to the clue list
    solved = 1 # set it to solved
  else: # otherwise
    solved = 0 # set it to unsolved
  return solved # return whether the puzzle was solved or not. This value gets captured and evaluated in the begining of each gallery

# This functions takes the list of clues and prints it.
# It first checks whether the user has clues, and tells them if they don't
# Then it prints whatever clues are there,
# With a relevant message about the user's next actions
def show_clues(clues):
    print()
    if len(clues) == 0: # If there are no clues to show
        print("You have no clues yet!") # print message
        print("Go visit some galleries!")
    else: # there are clues
        print("Your clues are:")
        for clue in clues: # print each clue in the list
            print(f"-{clue}")
        print()
        if len(clues) == 3: # If the user has all of their clues
            print("You have completed all of the challenges!")
            print("You are ready to make an escape") # prompt them to escape
        else: # If the user does not have all the clues
            print("You are missing clues.") # let them know
            print("Make sure to complete all of the galleries before you try to escape")
            print()



# This function ensures that the user has collected all of the clues
# Then it gives the user instructions for how order the clues
# If the user enters the right clue, it prints the congradulatory exit message
# It also updates the variable escape to end the game loop
# If the clue is not correct, the user loses a point
def attempt_escape(energy, clues, escape, name):
    print()
    if len(clues) != 3: # Flags if the user hasn't completed all of the galleries and sends them back
        print("You have not completed all of the rooms.")
        print("Please come back when you have solved all of the puzzles")
    else: # otherwise
        print("Order your clues by the descending value of their metal,")
        print("Then enter only the numbers in that order")
        print()
        while True: # validation loop, makes sure that the user put in an integer
            answer = input("Your answer: ")
            print()
            try:
                answer = int(answer)
            except ValueError:
                print("Please enter a set of numbers")
                continue
            else:
                break # If all converted well, end validation loop
        if answer == 613: # If the answer was correct
            print("=========================") # print the success message
            print(f" Congradulations, {name}!")
            print("=========================")
            print()
            print("You've successfully collected all of the clues")
            print("disabled the security system,")
            print(f"and escaped with {energy} energy points")
            print()
            print("The curator would be proud!")
            print("========================")
            escape = 1 # update the variable escape. This value gets captured in main and ends the game loop.
        else: # If the answer was wrong
            energy = reduce_energy(energy, 1) # take off energy
            print("Better luck next time")
            escape = 0 # keeps the escape variable the same
        return energy, escape # return energy and escape



# Main function
# Sets the accumulators and lists and prints the opening message
# Then it runs a loop of printing the menu,
# evaluating the user's choice of action, and
# running the appropriate functions
def main():
    energy = 10 # assign energy accumulator.
    clues = [] # assign clue list
    escape = 0 # assign varaible escape, which controls the sentinel loop that runs the game
    print("It's 5:59 PM. ") # opening message
    print("The museum is closing,")
    print("the security system is activating,")
    print("and you've discovered that the exit doors are locked!")
    print()
    print("Fortunately, the museum's eccentric curator")
    print("left behind a series of challenges.")
    print(" If you can solve the puzzles, collect the clues, ")
    print("and unlock the security system, you can escape.")
    print()
    name = input("What is your name, explorer? ")
    print()
    print(f"Welcome, {name}!")

    while escape != 1: # When the user ecapes, escape = 1. While it's not 1, the game runs
        if energy == 0: # If energy runs out
            print()
            print("OUT OF ENERGY! The museum remains locked. Game over.")
            break # game over
        else: # Otherwise
            show_menu(name, energy, clues) # Show the menu
            while True: # Input validation for menu options
                room = input("What is your next step? ")
                try:
                    room = int(room) # Ensure that room is an integer
                    if room < 1 or room > 6: # Ensure that the room is between 1 & 6, if it isn't
                        raise ValueError("Please inter a valid option") # Raise ValueError
                        continue # reprompt
                except ValueError as e: # if the input was not an integer
                    print("Please enter a valid option") # print message
                    continue # reprompt
                else: # if all is well
                  break # end validation loop
            #descision tree
            if room == 1:
                energy = gallery_one(clues, energy) # energy return for gallery one is stored in energy. Same for two and three
            elif room == 2:
                energy = gallery_two(clues, energy)
            elif room == 3:
                energy = gallery_three(clues, energy)
            elif room == 4:
                show_clues(clues)
            elif room == 5:
                energy, escape = attempt_escape(energy, clues, escape, name) # The user entered the correct code, escape = 1
            else: # If the user enters 6 to quit
                print("You quit, you lose") # Print message
                escape = 1 # set escape to 1, to end game loop
'''
Rebinding a list:
'''

list = ["Pomegranites", "Grapes", "Figs"]

def rebind_list(list):
    list.append("grapes") # A list is a mutable tye of data, so it can be added to from within a function
    print("I am the appended list:", list)
    list = ["Apples", "Oranges", "Bananas"]# This reassignment rebinds the list, but the new list only exists within the function. Once the function ends, the list disapearss.
    print("I am the list rebound: ", list)

rebind_list(list)
print("I am the list, post-function:", list)



main()

# Comments

# 1. The function for Gallery two was pretty hard. I wanted to
# do some form of input validation so that people couldn't just
# type anything. So it doesn't allow for numbers or special characters,
# even though it doesn't filter for real words.
# To do this, I had to figure out how to compare the letter to the alphabet,
# And ensure that the loop discarded any evaluation letters that were part of an invalid entry
# So it would reprompt for a valid entry instead of ending the loop

# 2. I returned values in each of the functions for the energy
# points, and the clue list. The calling code stored the returns # in their respective variables.

# 3. The mutation of teh list carried over outside of the function,
# whereas the rebound list only existed as log as the function did.
# After the function, the list reverted back to it's original content

# 4. The input validation for the escape code originally involved a sentinel loop
# that ended when the variable escape was either 0 or 1. The problem was, if someone entered
# the wrong escape code once, the loop would not run again because esape already equaled 0.
# So I took out the sentinel, and simply broke the loop after the answer was confirmed to be an integer,
# and I put the actual evaluation of the answer after the loop.