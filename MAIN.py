import os
import sys
import time

from LargeText import largeText

def clearCmdText(): # Clears all text on the command line interface, making it cleaner
    os.system('cls' if os.name == 'nt' else 'clear')

def slowPrint(str, speed=0.01): # Slowly prints out text
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def checkUserInput(inputList, displayOptions=True):
    flag = False
    while flag == False:
        if displayOptions == True:
            slowPrint("What will you do?")
            j=0
            for i in inputList: # Displays the options the user has (inputList)
                j = j+1
                slowPrint(str(j) + ". " + str(i))

        userInput = input("> ").lower() # Takes in input and lowers it

        try:        # Checks if the userInput is an integer or not
            int(userInput)
            isInteger = True
        except:
            isInteger = False

        if isInteger == True: # If the input is an integer, it will return the appropriate object of the list
            if int(userInput) > 0 and int(userInput) <= len(inputList):
                return inputList[int(userInput) - 1]

        else: # Takes in userList and checks if it matches with one of the available answers:
            for i in range(len(inputList)):
                if userInput == inputList[i].lower():
                    return inputList[i]
        if flag == False:
            slowPrint("Invalid Input: " + str(userInput))

def main():  
    # Introduction
    clearCmdText()
    print(largeText["SPYRIM"])
    slowPrint("")
    slowPrint("Press enter to start the game.")
    checkUserInput([""], False)
    clearCmdText()
    
    slowPrint("A few days ago, a client contacted you for a new job involving the King. He will give you a handsome reward if you were to assassinate the king for him, to advance his political career. With newfound motivation, you set off with equipment fit for the job and head straight to the castle. You sneak around outside of the castle and meet with a tall wall made of stone bricks. You look closer and see some bricks are conveniently sticking out of the wall")
    # First choice
    userChoice = checkUserInput(["Go home", "Climb"])
    clearCmdText()

    if userChoice == "Go home":
        slowPrint("You decide that this mission is not worth the risk. You go home and spend the rest of your life happily, not regretting the decision you made that day. (GOOD ENDING) ")
        time.sleep(7)
        clearCmdText()
        print(largeText["SUNSET"])
        time.sleep(15)
        exit()
    if userChoice == "Climb":
        slowPrint("You climb up the wall using the bricks that are sticking out. As you reach the top, you notice a balcony a jump away from where you are.")
        userChoice = checkUserInput(["Do a flip", "Jump across sneakily"])
        clearCmdText()
        if userChoice == "Do a flip":
            slowPrint("You flip across and hit your head on the railing of the balcony. You fall to your death. To be fair, it was a sick flip. ")
            time.sleep(7)
        if userChoice == "Jump across sneakily":
            slowPrint("You jump across the gap and reach the balcony of the castle. You look inside the room and see a large library with few signs of life. To the left you see the only person in this entire room. He is sitting on a chair with a table in front and newspaper over their head to hide the fact that he is sleeping on his job. When you saw that it was safe, you silently enter the room. Behind the guard there is a vent, and to the right of him there is an exit door.")
            # Second Choice
            userChoice = checkUserInput(["Go inside the vent", "Sneak through the door"])
            clearCmdText()

            if userChoice == "Go inside the vent":
                slowPrint("You sneak around the guard and go inside the vent. You hear a familiar tune from a certain one eyed astronaut. You ignore it and start crawling. It's a tight fit, but the rats that are skittering in the vent still find a way to go through you. It feels disgusting. The displeasure continues until you reach the first exit of the vent. You kick the vent open and crawl outside. Your stinky smell permeates throughout the room and immediately calls attention to the conglomerate of people inside. You are in the King's Throne Room. There seems to be a dinner party of some kind. Your target, the King, immediately calls for the guards to apprehend you.")
                # Third choice
                userChoice = checkUserInput(["Fight the guards", "Sneak away and chase after the king"])
                clearCmdText()
                if userChoice == "Fight the guards":
                    slowPrint("You try to fight the guards and you realize they are the king's guards for a reason. You realize how stupid it is to try to kill multiple military, high ranked, royal, ARMED guards. You are immediately skewered by their spears at the first sign of threat. (DEAD END)")
                    time.sleep(7)
                    clearCmdText()
                    print(largeText["DEATH"])
                    time.sleep(15)
                    exit()

                if userChoice == "Sneak away and chase after the king":
                    slowPrint("You throw a smoke bomb, stunning the guards, and chase after the king, who is pulling a lever behind the throne. You see a passage open behind the throne and the king go inside of it. Suddenly, two guards appear and block your way towards the passage. You look around and notice an exit door free from any guards, but it would mean abandoning your mission. The more you hesitate, the more the king gets away.")
                    userChoice = checkUserInput(["Escape through the exit door", "Chase after the king"])
                    clearCmdText()

                    if userChoice == "Escape through the exit door":
                        slowPrint("You run towards the exit doors and swiftly go through them. You briefly look and realize its the exterior of the castle, right above the tall wall. With quick thinking, you take out your grappling hook and attach it to the railing. While holding the rope, you rappel down the vertical wall and escape the castle. This peace would not last long, as you are a wanted man in this kingdom. With no one wanting to associate with a criminal, you live the rest of your life as an outlaw to the kingdom. (OUTLAW ENDING) ")
                        time.sleep(7)
                        clearCmdText()
                        print(largeText["OUTLAW"])
                        time.sleep(15)
                        exit()
                
                    if userChoice == "Chase after the king":
                        slowPrint("You chase after the king, fighting the guards along the way. The guards are more focused on keeping you away from the King. You briefly fight for way of passage and when they seemed most vulnerable you throw a knife to both of their necks, killing them instantly. After picking up one of the spears, you chase after the king and impale him right then and there. With no time to feel accomplished on a job well done, you run away and escape from the castle. Your client pays you with enough money to last 3 lifetimes and you live the rest of your life in luxury. (BLOODY LUXURY ENDING)")
                        time.sleep(7)
                        clearCmdText()
                        print(largeText["BLOOD"])
                        time.sleep(15)
            
            if userChoice == "Sneak through the door":
                slowPrint("You sneak through the door with the guard still asleep. You walk through a hallway with extravagant art and pottery, until you reach the only door in the hallway. You slowly open the door and the two guards right outside the door immediately notice you. They point their spears at you and are immediately arrested for breaking in to the castle. They take all of your belongings and lock you up in the castle's dungeon. (BAD ENDING) ")
                time.sleep(7)
                print(largeText["IMPRISONED"])
                time.sleep(15)
                






                


if __name__ == '__main__':
    main()

    