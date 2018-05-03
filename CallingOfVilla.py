# Tabs: 4 spaces

import mysql.connector
import time
from termcolor import colored, cprint
import pygame

# Commands go here | First person always. Ex. "I have *List of items*"
# TODO: Commands: use, talk, (read), (eat), quit, restart?, (save, load,) look at / for objects ADD elif for useStudyKey
# TODO: Triggers for all the doors opening, Study, Attic, Garden, Cellar, Voices done for the start, QBedroom and Walkway

def inventory():
    cur = db.cursor()
    sql = "SELECT Object_Id, Description FROM Object WHERE Location = PLAYER;"
    cur.execute(sql)
    if cur.rowcount()>=1:
        print("I have: ")
        for item in cur.fetchall():
            print("-" + item[0])
    else:
        print("I don't have anything at the moment.")
    return

def light():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Location = PLAYER and Object_Id = FLASHLIGHT"
    sqlTwo = "SELECT Object_Id FROM Object WHERE Location = PLAYER and Object_Id = LAMP"
    cur.execute(sql)
    if cur.rowcount()>=1:
        print("My flashlight is on.")
    else:
        print("I have nothing to light at the moment.")
    cur.execute(sqlTwo)
    if cur.rowcount()>=1:
        print("My oil lamp is on.")
    

 # AND SOURCE keskelle missä pelkkä AND??
def move(location, destination):
    destination = location
    cur = db.cursor()
    sql ="SELECT Location FROM Passage WHERE Direction." + Direction + "AND" + location + "AND Locked=0"
    cur.execute(sql)
    if cur.rowcount>=1:
            for row in cur.fetchall():
                destination = row[0]
    else:
        destination = location
    return destination

# Change to include objects aswell make it show the extra details after the i am in the; so fech desc and details separatetly
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
    sql = "UPDATE Object SET Location='PLAYER', Available=FALSE WHERE Refname='" + target + "' AND Location='" + location + "' AND Available=TRUE AND Takeable=TRUE;"
    cur.execute(sql)
    if cur.rowcount==1:
        print("I take the", target)
    else:
        print("I can't take that right now.")

# Events here:
def eventTrophyVoices():
    print("My head feels light ... more voices..?")
    cprint("...you boys hear about the servant girl?", 'magenta')
    cprint("...the one caught stealing from the master?", 'cyan')
    cprint("...I hear she is still hiding in that small room in the kitchen...", 'magenta')
    cprint("...let's hope that she has learned her lesson...", 'cyan')
    TrophyVoices = True
def eventWalkwayVoices():
    cprint("... once such a beautiful garden... I'll have to see what I can do about that... maybe you can visit sometime...", 'blue')
    WalkwayVoices = True

def eventQuestBedroomVoices():
    cprint("... I'm feeling peckish... they always said that the answer can be found on your plate", 'blue')
    QuestVoices = True



# Use triggers:
def useStudyKey():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='STUDYKEY' AND Location='PLAYER'"
    cur.execute(sql)
    if cur.rowcount()>=1:
        sql = "UPDATE Passage SET Locked='False' WHERE StartLocation='HALLWAY' AND Destination='STUDY';"
        cur.execute(sql)
        if cur.rowcount()>=1:
            print("The key I had opened the study.")
    else:
        print("I can't do that now.")



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
                            
# Initializing the emptyscreen, loading titles and resetting the location
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
print("Your name is", PlayerName, "and you are an aspiring blogger going to explore and old abandoned mansion to record your journey for money and fame.")
print("Your friend dropped of you at the edge of the forest and after a couple of hours of hiking, you have finally arrived at the old mansion.")
print("You enter the once magnificent building and hear the giant double doors lock behind your back.")
print("The old house seems creepier and creepier by the second, and you have to...")
# time.sleep(17)
print("... G E T  O U T...")
print("I can hear a whispy voice around me... I can almost make out the words...")
#time.sleep(3)
cprint("... you ever talk to animals? I find their company extremly revealing...", 'blue')
location = "MAINHALL" 
command = ""

# Main Loop
while command!="quit" and command!="exit" and location!="EXIT":
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
    # Inventory
    if command=="inventory" or command=="i":
        inventory()
    
    # Looking around
    elif command=="look":
        look()

    # Taking objects 
    elif command=="take" or command=="get" and target!="":
        getOK = getObject(target)
        # if getOK==1:
            # Things appearing if get here.

    # Movement 
    #TODO IS THAT QUEST BROOM SUPPOSED TO BE MASTER
    elif command=="north" or command=="east" or command=="south" or command=="west" or command=="n" or command=="e" or command=="s" or command=="w" \
        or command=="nw" or command=="sw" or command=="ne" or command=="se" or command=="northwest" or command=="southwest" or command=="northeast" or command=="southeast" \
        or command=="up" or command=="u" or command=="down" or command=="d":
        movedLocation = move(location, destination)
        if location == movedLocation:
            print("I can't move there")
        else:
            location = movedLocation
            look()
        if location=="QUESTBEDROOM" and QuestVoices==False:
            eventQuestBedroomVoices()
        if location=="WALKWAYBATH" and WalkwayVoices==False:
            eventWalkwayVoices()
        if location=="TROPHYROOM" and TrophyVoices==False:
            eventTrophyVoices()


    # Light command
    elif command=="light" or command=="l":
        light()

    # Audio Commands
    elif command=="play":
        playAudio()
    
    elif command=="stop":
        stopAudio()
    
    # Unknown Command
    elif command!="quit" and command!="exit" and command!="":
        print("I don't think I can",command)
    
   

if (location=="EXIT"):
    print("") # Victory speech here
else:
    print("Don't be gone too long...")
db.rollback()