import random
import os
import time

items = ["Door", "Mirror", "Crystal vase","Painting","Baloons", "Desk", "Phone",
          "Bookcase", "Champagne bottle",  "Shoes"]

result = []

# Randomize each number from three digit code
code_pt_1 = random.randint(0, 9)
code_pt_2 = random.randint(0, 9)
code_pt_3 = random.randint(0, 9)

# Randomize code location and make sure they don't overlap
code_loc_1 = random.randint(1, 3)
code_loc_2 = random.randint(4, 6)
code_loc_3 = random.randint(7, 9)

code = int(str(code_pt_1) + str(code_pt_2) + str(code_pt_3))

def clr_scr():
    """Clear screen helper"""

    # Check if operating system is Linux or Mac
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # Else operating system is Windows (os.name = nt)
        _ = os.system('cls')


def splash_start():
    print('''
      ______                             __                     
     |  ____|                           / _|                    
     | |__   ___  ___ __ _ _ __   ___  | |_ _ __ ___  _ __ ___  
     |  __| / __|/ __/ _` | '_ \ / _ \ |  _| '__/ _ \| '_ ` _ \ 
     | |____\__ \ (_| (_| | |_) |  __/ | | | | | (_) | | | | | |
     |______|___/\___\__,_| .__/ \___| |_| |_|  \___/|_| |_| |_|
         /\               | | |             | |                 
        /  \   _ __ ___  _|_| |_ ___ _ __ __| | __ _ _ __ ___   
       / /\ \ | '_ ` _ \/ __| __/ _ \ '__/ _` |/ _` | '_ ` _ \  
      / ____ \| | | | | \__ \ ||  __/ | | (_| | (_| | | | | | | 
     /_/    \_\_| |_| |_|___/\__\___|_|  \__,_|\__,_|_| |_| |_|                                                             
    ''')


def splash_end():
    print('''
      ______           _          __           
     |  ____|         | |        / _|          
     | |__   _ __   __| |   ___ | |_           
     |  __| | '_ \ / _` |  / _ \|  _|          
     | |____| | | | (_| | | (_) | |            
     |______|_| |_|\__,_|  \___/|_|         __ 
          | |               | |            /_ |
       ___| |__   __ _ _ __ | |_ ___ _ __   | |
      / __| '_ \ / _` | '_ \| __/ _ \ '__|  | |
     | (__| | | | (_| | |_) | ||  __/ |     | |
      \___|_| |_|\__,_| .__/ \__\___|_|     |_|
                      | |                      
                      |_|                      
    ''')

def intro():
    """ Game intro """

    splash_start()
    name = str(input("Enter your name:\n> "))
    clr_scr()
    print("You slowly open your eyes...\n")
    time.sleep(2)
    print("what the hell did I do last night...")
    print("my head is killing me.")
    time.sleep(1)
    print("Oh yeah... I'm in Amsterdam\n")
    time.sleep(2)
    print("You look around, room is trashed like there was a rockstar party inside.")
    print("There are bottles, clothes and half finished drinks everywere\n")
    time.sleep(2)
    print("Where is everybody?\n")
    time.sleep(2)
    print("On a night stand next to you there is a message\n")
    time.sleep(4)
    print("It's written in cursive on a thick paper,")
    print("you can smell the scent of women's parfume on it.")
    print("There is a kiss in the corner made of red lipstick.\n")
    print("It reads:\n")
    time.sleep(4)
    print("Dear " + name)
    print("welcome to AMS Liberia.")
    print("We hope you had a good night,")
    print("now, get ready for the first game.")
    print("Time is of essence and you have excatly 60 minutes")
    print("to find the combination and open the door.")
    print("If you fail, door will stay locked...Forever.")
    print("Good luck.")
    print("            Miss V")
    time.sleep(3)
    print("\nYou get up and after looking around identify several interesting items\n")


def door(code):
    print("Next to the door is a big digitall access keypad. On it, the terminal cursor is blinking waiting for you to ener the code.")
    print("You start typing...\n")
    while True:
        inputDigit1 = input("Enter first digit: ")
        if (len(inputDigit1) == 1) and (inputDigit1.isnumeric()):
            break
        print("INPUT ERROR! Only numbers 0-9 are allowed")

    while True:
        inputDigit2 = input("Enter second digit: ")
        if (len(inputDigit2) == 1) and (inputDigit2.isnumeric()):
            break
        print("INPUT ERROR! Enter number 0-9")

    while True:
        inputDigit3 = input("Enter third digit: ")
        if (len(inputDigit3) == 1) and (inputDigit3.isnumeric()):
            break
        print("INPUT ERROR! Enter number 0-9")

    enteredCode = int(str(inputDigit1) + str(inputDigit2) + str(inputDigit3))

    if enteredCode == code:
        time.sleep(1)
        clr_scr()
        print("Terminal digits turn green, and with a loud beep you hear the heavy door unlock. You carfully open the door and peek through the dimly lit hallway.")
        splash_end()
        return (1)
    else:
        print("Terminal digits start flashing red, giving annoyng tone of failure. INCORRECT CODE! ")
        return(0)

# def mirror()
# def crystal_vase()
# def painting()
# def baloons()
# def desk()
# def phone()
# def bookcase()
# def champagne_bottle()
# def shoes()

def main_menu(list, question):
    for item in list:
        print(list.index(item), item)

    while True:
        result = input(question)
        try:
            result = int(result)
            break
        except:
            print("Please enter a number between 0-9:")

    return result


while True:
    usr_choice = main_menu(items, "\nWhat do you want to investigate?\n> ")

    if usr_choice == 1:
        mirror(usr_choice, code_loc_1, code_pt_1)
    else:
        result = door(code)
    if result == 1:
        break

