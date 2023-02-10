import sys
import time


def print_slow(str, speed=0.00001):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)
    print()

'''
TODO
Replace input with multiple choice
Add color to text

'''
# Checks if string contains item in list, then returns the input as a list
def checkStr(dialogue, inputList, speed=0.00001, addText=True):
    flag = False
    while flag == False:
        print_slow(dialogue, speed)
        for i in range(len(inputList)):
            print(str(i+1) + ". " + str(inputList[i]))
        if addText == True: test_string = input("\nWhat will you do?\n")
        testList = test_string.split(" ")



        for i in testList:
            for j in inputList:
                if i==j or int(testList) > 0 and int(testList) <= len(inputList):
                    flag = True
                    return j
        if flag == False:
            print("Invalid Input: " + test_string)
