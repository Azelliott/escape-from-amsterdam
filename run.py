import random
from items import *

items = ["Door", "Mirror", "Crystal vase","Painting","Baloons", "Desk",  "Phone",
          "Bookcase", "Champagne bottle",  "Shoes"]
result = []

# Randomize code location and make sure they don't overlap
code_loc_1 = random.randint(1, 3)
code_loc_2 = random.randint(4, 6)
code_loc_3 = random.randint(7, 9)

# Create a list of 3 random numbers in the range 0-9
random_code = [random.randint(0, 9) for i in range(3)]

# Create a 3 digit code from the random list
full_code = int(str(random_code[0]) + str(random_code[1]) + str(random_code[2]))

# Main menu
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


#intro()
while True:
    usr_choice = main_menu(items, "\nWhat do you want to investigate?\n> ")
    clr_scr()
    match usr_choice:
       case 1:
          baloons(usr_choice, code_loc_1, random_code[0])
       case 2:
          desk(usr_choice, code_loc_1, random_code[0])
       case 3:
          crystal_vase(usr_choice, code_loc_1, random_code[0])
       case 4:
          phone(usr_choice, code_loc_2, random_code[1])
       case 5:
          painting(usr_choice, code_loc_2, random_code[1])
       case 6:
          bookcase(usr_choice, code_loc_2, random_code[1])
       case 7:
          champagne_bottle(usr_choice, code_loc_3, random_code[2])
       case 8:
          mirror(usr_choice, code_loc_3, random_code[2]) 
       case 9:
          shoes(usr_choice, code_loc_3, random_code[2])
       case _:
          result = door(full_code)
    if result == 1:
        break