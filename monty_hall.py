"""a progrom to emulate and run the monty hall problem
where contestants are given 3 doors, behind two doors is a goats and behind
one door is a real cars. When the contestant choses a door the host tells the 
contestant to chose again after opening a door with a goats behind.
The host always opens the door of a goats
this code prints out the amount of times you would get cars or goats by chosing 
to swap or not"""

import random

def selectDoor():
    """initialise the starting of the game by shuffling the 'doors' and picking
    a choice there at random... i guess line 9 makes this a lot more random"""

    choices = ['goat', 'goat', 'car'] # the door beind each as such
    random.shuffle(choices) # shuffle the doors

    myChoiceInd = random.randint(0, 2) # pick a random int(0 to 2)

    myChoice = choices[myChoiceInd] # pick a door with the random int

    del choices[myChoiceInd] # remove the selected element, it already in myChoice

    return([myChoice, choices])

def openDoor(choices):
    """Simulates the idea of the host opening the door containing a goats
    and removing it from the list or doors"""
    choices.remove('goat')
    return(choices)

def increments(myChoice, cars, goats):
    """cars and goats variables are lists and this function increments them each 
    time, the else statement of the if block is for debuggin"""
    if myChoice == 'car':
        cars += 1
    elif myChoice == 'goat':
        goats += 1
    else:
        print("Error at increment()")

    return([cars, goats])

def swapFunc(myChoice, choices):
    """simulates the idea of the contestant swapping. there is only one element
    in the list and this function returns that choice
    if you print out the list of choices at this stage you would realise there
    is only one element, because
    1. after the contestant chose a door that door should no longer be counted 
    and hence it was removed
    2. after the host opened the door with a goats, the first goats in the list
    was removed... although it was the first goats it is still random becuase 
    the list was shuffled"""
    
    myChoice = choices[0]
    return(myChoice)

def crux(number, swap):
    """as the name of the function this is the crux of the matter where
    we loop for the number of times we want to carsry this out"""

    cars, goats = 0, 0

    for num in range(number):
        initialised = selectDoor() # init and select a door
        myChoice = initialised[0] #get your choice
        choices = initialised[1] # get your init list

        choices = openDoor(choices) # get a goats removed

        if swap == True:
            """if the contestant wants to swap"""
            myChoice = swapFunc(myChoice, choices)

        incremented = increments(myChoice, cars, goats)
        cars = incremented[0]
        goats = incremented[1]

    return([cars, goats])

def mainOutput(number, swap):
    """the main procesess are done in crux() this function is to format and 
    output the data
    number is the operation count and swap is if you want to swap the door"""
    stats = crux(number, swap) # get the data

    if swap == False:
        # binary statement is for the output to make sense
        binary_statment = "with no swaps"
    else:
        binary_statment = "with swaps"

    cars = stats[0]
    goats = stats[1]

    printStatement = f"Out of {number} times, {binary_statment}, cars came out "
    printStatement += f"{cars} times and goats came out {goats} times."

    print(printStatement)

if __name__ == '__main__':
    mainOutput(number=1000000, swap=False)