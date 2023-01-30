import time, sys
def print_slow(str, speed=0.00001):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(speed)



# Checks if string contains item in list, then returns the input as a list
def checkStr(dialogue, input_list, speed=0.00001, addText=True):
    flag = False
    while flag == False:
        print_slow(dialogue, speed)
        if addText == True: test_string = input("\nWhat will you do?\n")
        test_list = test_string.split(" ")
        for i in test_list:
            for j in input_list:
                if i==j:
                    flag = True
                    return j
        if flag == False:
            print("Invalid Input: " + test_string)
