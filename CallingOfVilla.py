# Tabs: 4 spaces

import mysql.connector
import time
from termcolor import colored

# Commands go here | First person always. Ex. "I have *List of items*"
# TODO: Commands: go, take, use, light, look, talk, (read), (eat), quit, restart?, (save, load, audio-on/off?) 

def inventory():
    cur = db.cursor()
    sql = "SELECT ObjectId, Description FROM Object WHERE Location = Player;"
    cur.execute(sql)
    if cur.rowcount()>=1:
        print("I have: ")
        for item in cur.fetchall():
            print("-" + item[0])
    else:
        print("I don't have anything at the moment.")
    return

# Connection here
# db = mysql.connector.connect(host="localhost",
#                            user="",
#                            passwd="",
#                            db="CallingOfVilla",
#                            buffered=True)

                            
# Initializing the location and an empty screen
print("\n"*1000)
logo =colored('''
 _______  _______  _        _       _________ _        _______    _______  _______            _________ _        _        _______ 
(  ____ \(  ___  )( \      ( \      \__   __/( (    /|(  ____ \  (  ___  )(  ____ \  |\     /|\__   __/( \      ( \      (  ___  )
| (    \/| (   ) || (      | (         ) (   |  \  ( || (    \/  | (   ) || (    \/  | )   ( |   ) (   | (      | (      | (   ) |
| |      | (___) || |      | |         | |   |   \ | || |        | |   | || (__      | |   | |   | |   | |      | |      | (___) |
| |      |  ___  || |      | |         | |   | (\ \) || | ____   | |   | ||  __)     ( (   ) )   | |   | |      | |      |  ___  |
| |      | (   ) || |      | |         | |   | | \   || | \_  )  | |   | || (         \ \_/ /    | |   | |      | |      | (   ) |
| (____/\| )   ( || (____/\| (____/\___) (___| )  \  || (___) |  | (___) || )          \   /  ___) (___| (____/\| (____/\| )   ( |
(_______/|/     \|(_______/(_______/\_______/|/    )_)(_______)  (_______)|/            \_/   \_______/(_______/(_______/|/     \|
                                                                                                                                                                                                                                                    
''', 'red')
print(logo)
time.sleep(3)
house = colored('''
            
               *         .              *            _.---._      
                             ___   .            ___.'       '.   *
        .              _____[LLL]______________[LLL]_____      |
                      /     [LLL]              [LLL]     \     |
                     /____________________________________\    |    .
                      )==================================(    /
     .      *         '|I .-. I .-. I .--. I .-. I .-. I|'  .'
                  *    |I |+| I |+| I |. | I |+| I |+| I|-'`       *
                       |I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I|      .
              .       _|I_____I_____I______I_____I_____I|_
                       )================================(   *
       *         _     |I .-. I .-. I .--. I .-. I .-. I|          *
                |u|  __|I |+| I |+| I |<>| I |+| I |+| I|    _         .
           __   |u|_|uu|I |+| I |+| I |~ | I |+| I |+| I| _ |U|     _
       .  |uu|__|u|u|u,|I_|+|_I_|+|_I_|__|_I_|+|_I_|+|_I||n|| |____|u|
          |uu|uu|_,.-' /I_____I_____I______I_____I_____I\`'-. |uu u|u|__
          |uu.-'`      #############(______)#############    `'-. u|u|uu|
         _.'`              ~"^"~   (________)   ~"^"^~           `'-.|uu|
      ,''          .'    _                             _ `'-.        `'-.
  ~"^"~    _,'~"^"~    _( )_                         _( )_   `'-.        ~"^"~
      _  .'            |___|                         |___|      ~"^"~     _
    _( )_              |_|_|          () ()          |_|_|              _( )_
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/[===]\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
    |_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_|_|
    |___|/\/\/\/\/\/\/\|___|/\/\/\/\/\|| ||/\/\/\/\/\|___|/\/\/\/\/\/\/\|___|
~""~|_|_|\/\/\/\/\/\/\/|_|_|\/\/\/\/\/|| ||\/\/\/\/\/|_|_|\/\/\/\/\/\/\/|_lc|~""~
   [_____]            [_____]                       [_____]            [_____]

''','white')
print(house)


PlayerName = input("Give me your name: ")
print("Your name is",PlayerName,"and you are an aspiring blogger going to explore and old abandoned mansion to record your journey for money and fame.")
print("Your friend dropped of you at the edge of the forest and after a couple of hours of hiking, you have finally arrived at the old mansion.")
print("You enter the once magnificent building and hear the giant double doors lock behind your back.")
print("The old house seems creepier and creepier by the second, and you have to...")
time.sleep(17)
print("... G E T  O U T...")
location = "MAINHALL"
command = ""

# Main Loop
while command != "quit" and location != "END":
    print("")
    operation = input("What to do: ").split()
    # The user's command is taken
    if len(operation)>=1:
        command = operation[0].lower()
    else:
        print("")
    # If the command is longer than 1, we take the target here by selecting the last item in the command
    if len(operation)>=2:
        target = operation[len(operation)-1].lower()
    else:
        target = ""
    # Print an empty line for readability
    print("")
    #All of the action come here vvv
    if command=="inventory" or command=="i":
        inventory()
    
    elif command!="quit" and command!="":
        print("I don't think I can",command)
    

if (location=="EXIT"):
    print("") # Victory speech here
else:
    print("Don't be gone too long...")
db.rollback()