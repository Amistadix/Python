print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input('You are stuck at a crossroads. Where do you wanna go - left or right?')

if crossroad == "right":
    print("You fell into a hole! Game Over")
elif crossroad == "left":
    lake = input("You arrive at the shore of a big lake. Do you want to WAIT for the boat or SWIM?\n")
    if lake == "swim":
        print("You were eaten by a crocodile! Game over")
    elif lake == "wait":
        door = input("You crossed the lake safely. You have three doors to choose: red, blue or yellow?\n")
        if door == 'blue':
            print('You were eaten by a blue dragon. Game over!')
        elif door == "yellow":
            print('You were eaten by the golden dragon. Game over!')
        elif door == "red":
            print('Congratulations! You found the treasure!')
else:
    print('You made a wrong choice. Game over!')