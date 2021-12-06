import random

def StartInsult():
    # Start the process of getting input to make the insults
    while True:
        getInput()

def getInput():
    # Getting Input from User for number of insults
    try:
        InsultNum = input("Please enter the number of insults you would like to generate: ")

        if (not InsultNum.isdigit()):
            print("*** ERROR - The number of Insults must be a number! ***")
            return getInput()
        elif (int(InsultNum) == 0):
            print("*** ERROR - The number must be 1 or more! ***")
            return getInput()
        elif (int(InsultNum) < 1):
            print("*** ERROR - The number of Insults must be a positive number! ***")
            return getInput()
    except ValueError:
        print("*** ERROR - The number of Insults must be a number! ***")
        return getInput()
        
    # Getting Input from user for name used in insult & If string is empty tell user and shut down
    VictimName = input("Please enter Victims name: ")
    if (str(VictimName) == ""):
        print("*** ERROR - The name cannot be empty! ***")
        return getInput()

    # Check to see if string is only letter and not numbers
    elif (VictimName.isalpha() == False):
        print("*** ERROR - The name must only be letters ***")
        return getInput()


    # Getting Input from user for how many adjectives to put in insult & Error checking to make sure user enters whole number
    try:
        AdjectNum = int(input("Please enter how many adjectives in insult: "))
        AdjectCheck(InsultNum, VictimName, AdjectNum)
    # Check to make sure that it is not an empty value and that it is a number not a letter
    except ValueError:
        print("*** ERROR - The number of adjectives must be a whole number between 1 and 3! ***")
        return getInput()

def AdjectCheck(InsultNum, VictimName, AdjectNum):
    # Checking to see if number of Adjective is between 1 and 3
    if (AdjectNum >= 1 and AdjectNum <= 3):
        GenerateInsults(InsultNum, VictimName, AdjectNum)

    # If the adjective number is not between 1 and 3 the program will tell user and shut down
    else:
        print("*** ERROR - The number of adjective must be a between 1 and 3! ***")
        return getInput()


def GenerateInsults(InsultNum, VictimName, AdjectNum):
    # lists of nouns and adjectives that the insult can contain
    AdjectiveList = ["smelly", "stinky", "dirty", "gross", "nasty", "toxic", "vulgar", "rude", "bitter", "intolerable"]
    NounList = ["dipstick", "jerk", "jackass", "dunce", "cow", "troglodyte"]

    # Loop to create the insults
    for i in range(int(InsultNum)):

        # Set insult back for each loop after it has been cleared
        Insult = [VictimName + " is a"]

        # Add the adjective to the end of the insult which will later have noun appened
        for i in range(AdjectNum):
            AdjectSelect = random.choice(AdjectiveList)
            Insult.append(AdjectSelect)

        # Add the Noun to the end of the insult which will later be converted to a string
        for i in range(1):
            NounSelect = random.choice(NounList)
            Insult.append(NounSelect)

        # convert list into sentence and seperate list items with spaces
        print(' '.join(Insult) + "!")
        
        # Reset the list for the next insult if more than one has been requested by user
        Insult.clear()
        
    # Once loop is done restart the entire program   
    # StartInsult()    

StartInsult()