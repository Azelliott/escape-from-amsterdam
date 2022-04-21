import time
import os


def clr_scr():
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


def mirror(usr_choice, code_loc, code_val):
    print("You approach a big mirror and take a good look at yourself.\n '...Man I look like s*it'")
    if usr_choice == code_loc:
        print("As you are about to turn away, you notice that you are wearing unfamiliar t-shirt with a number " +
              str(code_val) + " on it.\n")
    else:
        print("There's no code here, you turn around.\n")


def crystal_vase(usr_choice, code_loc, code_val):
    print("You approach expensive looking crystal vase")
    if usr_choice == code_loc:
        print("There is gold plated insignia 'Liberia' and a number " +
              str(code_val) + " above it.\n")
    else:
        print("'I better not touch this too much or I might brake it.' You move away.\n")


def painting(usr_choice, code_loc, code_val):
    print("You come closer to the big work of art on the wall. Looks old")
    if usr_choice == code_loc:
        print("After admiring the painting for few moments, your glance registers something weird. Signature reads Lib-" + str(code_val) + ".")
    else:
        print("'I don't have time to admire fine art, need to find the codes to escape from this place.' No code found.\n")


def baloons(usr_choice, code_loc, code_val):
    print("In the corner, there is several helium filled ballons.You come closer.")
    if usr_choice == code_loc:
        print("Few brightly colored helium ballons, at the back, somewhat hidden is a small baloon shaped like a number " + str(code_val) + ".\n")
    else:
        print("'Who brought these here? I don't remember anybody had ballons yesterday...' There is no code here.\n")


def desk(usr_choice, code_loc, code_val):
    print("You come to the big walnut work desk in the corner of the room.")
    if usr_choice == code_loc:
        print("After carefully going through all the things, you see a letter seal with a " +
              str(code_val) + " on it.\n")
    else:
        print("You looked everywhere but you couldn't find the code.\n")


def phone(usr_choice, code_loc, code_val):
    print("There is a vintage rotary phone next to the Door")
    if usr_choice == code_loc:
        print("As you come closer you realize that every number on the dial is number " +
              str(code_val) + ".\n")
    else:
        print("You pick up the phone but there was no sound. 'It was kinda expected, but still...gave me a bit of hope'\n")


def bookcase(usr_choice, code_loc, code_val):
    print("Luxurious looking bookcase with brass details.")
    if usr_choice == code_loc:
        print("You start reading the titles and sifting through the books hoping to find the clue.")
        print("Suddenly small note falls out of one of them. On it says: 'seek and ye shall find' and a number " +
              str(code_val) + " below it.\n")
    else:
        print("You couldn't find any code.\n")


def champagne_bottle(usr_choice, code_loc, code_val):
    print("A pretty big champagne bottle.")
    if usr_choice == code_loc:
        print("You see " +
              str(code_val) + " marbles inside. How did they get in there.\n")
    else:
        print("'Never again'. You thought to yourself...again. No code or alcohol here\n")


def shoes(usr_choice, code_loc, code_val):
    print("There is several shoes in the hallway, none of them is yours.")
    if usr_choice == code_loc:
        print("You realize that all " + str(code_val) +
              " of them are left.\n")
    else:
        print("No code here. 'Don't know what did I expect to find.'\n")


def door(full_code):
    while True:
        inputDigit1 = input("Enter first digit: ")
        inputDigit2 = input("Enter second digit: ")
        inputDigit3 = input("Enter third digit: ")

        enteredCode = str(inputDigit1) + str(inputDigit2) + str(inputDigit3)

        if (len(enteredCode) == 3) and (enteredCode.isnumeric()):
            break
        print("INPUT ERROR! Only numbers 0-9")

    if int(enteredCode) == full_code:
        time.sleep(1)
        clr_scr()
        print("Terminal digits turn green, and with a loud beep you hear the heavy door unlock. You carfully open the door and peek through the dimly lit hallway.")
        splash_end()
        return (1)
    else:
        print("Terminal digits start flashing red, giving annoyng tone of failure. INCORRECT CODE!\n")
        return(0)
