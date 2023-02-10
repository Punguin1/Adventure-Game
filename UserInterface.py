from SpyrimFunc import print_slow
from SpyrimFunc import checkStr as cs
import sys, time, os

def clearCmdText(): # Clears all text on the command line interface, making it cleaner
    os.system('cls' if os.name == 'nt' else 'clear')
def slowPrint(str, speed=0.00001):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()
def checkUserInput(inputList):
    flag = False
    while flag == False:
        slowPrint("What will you do?")
        j=0
        for i in inputList:
            j = j+1
            slowPrint(str(j) + ". " + str(i))
        userInput = input("> ").split(" ") # Takes user input, lowercases it, and makes it into a list. On the following code, it will convert from string and from string to integer in order to read the input and the type of data it is
        print(userInput)
        try:        # Checks if the userInput is an integer or not
            int(str(userInput))
            isInteger = True
        except:
            isInteger = False

        if isInteger == True:
            if int(str(userInput)) > 0 and int(str(userInput)) <= len(inputList):
                return inputList[int(userInput) - 1]
        else:
            for i in userInput:
                for j in inputList:
                    if i == j:
                        return j
            if flag == False:
                slowPrint("Invalid Input: " + str(userInput))


slowPrint("This is test writing")
print(checkUserInput(["poop", "tweet"]))
    