"""a progrom to emulate and run the monty hall problem
where contestants are given 3 doors, behind two doors are goats and behind
one door is a real car. When the contestant choses a door the host gives the 
option for the contestant to chose again(or swap the door) after opening a door
with a goats behind. The host always opens the door of a goat.
this code prints out the amount of times, for the amount of times iterated,
you would get cars or goats by chosing to swap or not"""

from random import shuffle, randint

class MontyHallProb():
    """docstring for MontyHallProb"""
    def __init__(self, number, swap):
        self.number =  number
        self.swap = swap

    def selectDoor(self):
        """initialise the starting of the game by shuffling the 'doors' and picking
        a choice there at random... i guess line 9 makes this a lot more random"""

        choices = ['goat', 'goat', 'car'] # the door beind each as such
        shuffle(choices) # shuffle the doors

        myChoiceInd = randint(0, 2) # pick a random int(0 to 2)

        myChoice = choices[myChoiceInd] # pick a door with the random int

        del choices[myChoiceInd] # remove the selected element, it already in myChoice

        return([myChoice, choices])

    def openDoor(self, choices):
        """Simulates the idea of the host opening the door containing a goats
        and removing it from the list or doors"""
        choices.remove('goat')
        return(choices)

    def increments(self, myChoice, cars, goats):
        """cars and goats variables are lists and this function increments them each 
        time, the else statement of the if block is for debuggin"""
        if myChoice == 'car':
            cars += 1
        elif myChoice == 'goat':
            goats += 1
        else:
            print("Error at increment()")

        return([cars, goats])

    def swapFunc(self, myChoice, choices):
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

    def crux(self):
        """as the name of the function this is the crux of the matter where
        we loop for the number of times we want to carsry this out"""

        cars, goats = 0, 0

        for num in range(self.number):
            initialised = self.selectDoor() # init and select a door
            myChoice = initialised[0] #get your choice
            choices = initialised[1] # get your init list

            choices = self.openDoor(choices) # get a goats removed

            if self.swap == True:
                """if the contestant wants to swap"""
                myChoice = self.swapFunc(myChoice, choices)

            incremented = self.increments(myChoice, cars, goats)
            cars = incremented[0]
            goats = incremented[1]

        return([cars, goats])

    def printStats(self):
        """the main procesess are done in crux() this function is to format and 
        output the data
        number is the operation count and swap is if you want to swap the door"""
        stats = self.crux() # get the data

        if self.swap == False:
            # binary statement is for the output to make sense
            binary_statment = "with no swaps"
        else:
            binary_statment = "with swaps"

        cars = stats[0]
        goats = stats[1]

        printState = f"Out of {self.number} times, {binary_statment}, cars came"
        printState += f" out {cars} times and goats came out {goats} times."

        print(printState)

if __name__ == '__main__':

    round1 = MontyHallProb(1000000, True)
    round1.printStats()