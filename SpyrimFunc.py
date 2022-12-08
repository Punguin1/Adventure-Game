import time, sys
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.003)



# Checks if string contains item in list, then returns the input as a list
def checkStr(dialogue, input_list):
    flag = False
    while flag == False:
        print_slow(dialogue)
        test_string = input("\n::")
        test_list = test_string.split(" ")
        for i in test_list:
            for j in input_list:
                if i==j:
                    flag = True
                    return j
        if flag == False:
            print("Invalid Input: " + test_string)
