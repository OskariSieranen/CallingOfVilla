# Tabs: 4 spaces

import mysql.connector
import time
from termcolor import colored
import pygame

# Commands go here | First person always. Ex. "I have *List of items*"
# TODO: Commands: go, use, light, talk, (read), (eat), quit, restart?, (save, load,) 

def inventory():
    cur = db.cursor()
    sql = "SELECT Object_Id, Description FROM Object WHERE Location = Player;"
    cur.execute(sql)
    if cur.rowcount()>=1:
        print("I have: ")
        for item in cur.fetchall():
            print("-" + item[0])
    else:
        print("I don't have anything at the moment.")
    return

def look():
    cur = db.cursor()
    sql = "SELECT Description, Details FROM Location WHERE ID='" + location + "';"
    cur.execute(sql)
    print("I am in the: ")
    for row in cur:
        print (row[0])
        if (row[1]!=""):
            print(row[1])

def getObject(target):
    cur = db.cursor()
    sql = "UPDATE Object SET Location='Player', Available=FALSE WHERE Refname='" + target + "' AND Location='" + location + "' AND Available=TRUE AND Takeable=TRUE"
    cur.execute(sql)
    if cur.rowcount==1:
        print("I take the", target)
    else:
        print("I can't take that right now.")

def playAudio():
    pygame.mixer.music.play()

def stopAudio():
    pygame.mixer.music.stop()
# Connection here
# db = mysql.connector.connect(host="localhost",
#                            user="",
#                            passwd="",
#                            db="CallingOfVilla",
#                            buffered=True)

# Initializing the music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('TestSong.wav')
pygame.mixer.music.play()
                            
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
# time.sleep(17)
print("... G E T  O U T...")
location = "MAINHALL"
command = ""

# Main Loop
while command!="quit" and command!="exit" and location!="END":
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
    
    elif command=="look":
        look()
    
    elif command=="take" or command=="get" and target!="":
        getOK = getObject(target)
        # if getOK==1:
            # Things appearing if get here.

    # Audio Commands
    elif command=="play":
        playAudio()
    
    elif command=="stop":
        stopAudio()
    
    # Unknown Command
    elif command!="quit" and command!="":
        print("I don't think I can",command)
    
   

if (location=="EXIT"):
    print("") # Victory speech here
else:
    print("Don't be gone too long...")
db.rollback()