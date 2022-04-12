# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random
import os
import time



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

intro()