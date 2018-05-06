# Tabs: 4 spaces

import mysql.connector
import time
from termcolor import colored, cprint
import pygame

# Commands go here | First person always. Ex. "I have *List of items*"
# TODO: Commands: inspect object?t
# TODO: add appearing of keys to the dining hall and library Fix 

def inventory():
    cur = db.cursor()
    sql = "SELECT Object_Id, Description FROM Object WHERE Location = 'PLAYER';"
    cur.execute(sql)
    res = cur.fetchall()
    if cur.rowcount>=1:
        print("I have: ")
        for item in res:
            print("- " + item[0])
    else:
        print("I don't have anything at the moment.")

def light():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Location = 'PLAYER' AND Object_Id = 'FLASHLIGHT';"
    sqlTwo = "SELECT Object_Id FROM Object WHERE Location = 'PLAYER' AND Object_Id = 'LAMP';"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("My flashlight is on.")
    else:
        print("I have nothing to light at the moment.")
    cur.execute(sqlTwo)
    if cur.rowcount>=1:
        print("My oil lamp is on.")
    
def move(location, direction):
    direction = location
    cur = db.cursor()
    sql = "SELECT Destination FROM Passage WHERE Direction='" + command + "' AND StartLocation='" + location + "' AND Locked=0;"
    cur.execute(sql)
    if cur.rowcount>=1:
            for row in cur.fetchall():
                direction = row[0]
    else:
        direction = location
    return direction

#TODO Change to include objects aswell make it show the extra details after the i am in the; so fech desc and details separatetly
def look():
    cur = db.cursor()
    sql = "SELECT Description, Details FROM Location WHERE Location_Id='" + location + "';"
    cur.execute(sql)
    print("I am in the: ")
    for row in cur:
        print (row[0])
        if (row[1]!=""):
            print(row[1])

def eatObject(target):
    cur = db.cursor()
    sql = "UPDATE Object SET Location='PLAYER', Available=FALSE WHERE Refname='" + target + "' AND Location='" + location + "' AND Available=TRUE AND Takeable=FALSE;"
    cur.execute(sql)
    if cur.rowcount==1 and target=="newspaper" or target=="food" or target=="pillow":
        print("I ate", target)
    else:
        print("I can't eat that.")

def readObject(target):
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_id='NEWSPAPER' OR Object_id='MANIFEST' OR Object_id='BIOGRAPHY'"
    #sql = "UPDATE Object SET Location='PLAYER', Available=FALSE WHERE Refname='" + target + "' AND Location='" + location + "' AND Available=TRUE AND Takeable=FALSE;"
    cur.execute(sql)
    if cur.rowcount>=1 and target=="newspaper" and location=="STUDY":
        sql = "SELECT Details FROM Object WHERE Object_Id='NEWSPAPER'"
        newspaperText = cur.execute(sql)
        print("Hmm what does it say?", newspaperText)
    elif cur.rowcount>=1 and target=="biography" and location=="LIBRARY":
        print("Hmm what is this?" , "Major depressive disorder descended upon writer" ,PlayerName, "during their college and young professional days, after a lifetime of loneliness and longing for family. Like many individuals suffering from this agonizingly common condition, she turned towards substance abuse and even a suicide attempt as a means of self-medicating. But a combination of steel will and a determined doctor set Wurtzel back on the difficult road to recovery.")
        print("What the hell is going on???")
        print("A sturdy iron key drops from between the pages of the biography...")
        sql = "UPDATE Object SET Location='PLAYER' , Available=FALSE WHERE Object_Id='ATTICKEY'"
        cur.execute(sql)
    elif cur.rowcount>=1 and target=="manifest" and location=="STUDY":
        sql = "SELECT Details FROM Object WHERE Object_Id='MANIFEST'"
        manifestText = cur.execute(sql)
        print("It's and old manifest of the books in the library. It's mostly destroyed by time, but I can still make out the location of a biography in the library... I wonder if it is still readable.")
    else:
        print("There is nothing to read.")

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
    #time.sleep(3)
    cprint("...you boys hear about the servant girl?", 'magenta')
    #time.sleep(3)
    cprint("...the one caught stealing from the master?", 'cyan')
    #time.sleep(3)
    cprint("...I hear she is still hiding in that small room in the kitchen...", 'magenta')
    #time.sleep(3)
    cprint("...let's hope that she has learned her lesson...", 'cyan')
    
def eventWalkwayVoices():
    cprint("... once such a beautiful garden... I'll have to see what I can do about that... maybe you can visit sometime...", 'blue')
    
def eventMasterBedroomVoices():
    cprint("... I'm feeling peckish... they always said that the answer can be found on your plate...", 'blue')

def eventAtticVoices():
    cprint("...I wonder if he is ok...", 'cyan')
    #time.sleep(3)
    cprint("...mhmhmhmhmhmhmhmhhhm...", 'yellow')
    #time.sleep(3)
    cprint("...I agree, he does look a bit different from the last time, maybe even worse...", 'cyan')
    #time.sleep(3)
    cprint("...mhmhmhmhmhmhmmhhmmhmhm...", 'yellow')
    #time.sleep(3)
    cprint("...I hope so too...", 'cyan')

def eventQuestBedroomFall():
    print("It is really dark in here...")
    time.sleep(3)
    print("DAMN... I fell and now my clothes are all covered in something sticky...")

def eventRiddleDoorOpening():
    cur = db.cursor()
    sql = "UPDATE Passage SET Locked=False WHERE StartLocation='RIDDLEROOM' AND Destination='WELL'"
    cur.execute(sql)
    print("The east wall of the room crumbles as I utter the word...")

def eventFinalRoom():
    cur = db.cursor()
    sql = "UPDATE Passage SET Locked=False WHERE StartLocation='WELL' AND Destination='THEEND'"
# Take triggers:
# def takeLadder():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='LADDER'"
#     cur.execute(sql)

# def takeStudyKey():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='STUDYKEY'"
#     cur.execute(sql)

# def takeAtticKey():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='ATTICKEY'"
#     cur.execute(sql)

# def takeGlimmer():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='GLIMMER'"
#     cur.execute(sql)

# def takeBucket():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='BUCKET'"
#     cur.execute(sql)

# def takeLamp():
#     cur = db.cursor()
#     sql = "UPDATE Object SET Location='PLAYER' , Available='False' WHERE Object_Id='LAMP'"
#     cur.execute(sql)

# Use triggers:
def useStudyKey():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='STUDYKEY' AND Location='PLAYER';"
    cur.execute(sql)
    if cur.rowcount>=1:
        sql = "UPDATE Passage SET Locked='False' WHERE StartLocation='HALLWAY' AND Destination='STUDY';"
        cur.execute(sql)
        if cur.rowcount>=1:
            print("The key I had opened the study.")
    else:
        print("I can't do that now.")

def useAtticKey():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='ATTICKEY' AND Location='PLAYER';"
    cur.execute(sql)
    if cur.rowcount>=1:
        sql = "UPDATE Passage SET Locked='False' WHERE StartLocation='HALLWAY' AND Destination='ATTIC';"
        cur.execute(sql)
        if cur.rowcount>=1:
            print("The key I had opened the door to the attic.")
        else:
            print("I can't do that now.")
            
def useGlimmer():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='GLIMMER' AND Location='PLAYER';"
    cur.execute(sql)
    if cur.rowcount>=1:
        sql = "UPDATE Passage SET Locked='False' WHERE StartLocation='TROPHYROOM' AND Destination='RIDDLEROOM';"
        cur.execute(sql)
        if cur.rowcount>=1:
            print("The key I had opened the door to the Basement.")
        else:
            print("I can't do that now.")

def useLadder():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='LADDER' AND Location='PLAYER';"
    cur.execute(sql)
    if cur.rowcount>=1:
        sql2 = "UPDATE Passage SET Locked='FALSE' WHERE StartLocation='MAINHALL' AND Destination='MIDDLEROOM';"
        cur.execute(sql2)
        print("I can now get to the second floor.")
        # if cur.rowcount>=1:
        #     print("I finally got to the second floor.")
        # else:
        #     print("I can't do that now.")

def useAtticSwitch():
    cur = db.cursor()
    sql = "UPDATE Passage SET Locked='False' WHERE StartLocation='MAINHALL' AND Destination='GARDENENTRANCE';"
    cur.execute(sql)
    print("I hear rumbling from downstairs...")

def useBucket():
    cur = db.cursor()
    sql = "SELECT Object_Id FROM Object WHERE Object_Id='BUCKET' AND Location='PLAYER';"
    cur.execute(sql)
    if cur.rowcount>=1:
        sql = "SELECT Object_Id FROM Object WHERE Object_Id='CAMERA';"
        cur.execute(sql)
        if cur.rowcount>=1:
            print("What is this? It's... Uhmm.. What?? I forgot my camera? Why is it here?")
            print("*The camera contains 10 different photos of you inside the mansion.. Last photo was takes 6 minutes ago. In the last picture you are in middle of the garden... The garden is burning all around you...")
            print("WHAT IS HAPPENING?! IS SOMEONE ELSE HERE?? WHO ARE YOU?? SHOW YOURSELF!")
            sql = "UPDATE Passage SET Locked=False WHERE StartLocation='WELL' AND Destination='THEEND'"
            cur.execute(sql)

        else:
            print("I can't do that now.")
def loseFlashlight():
    cur = db.cursor()
    sql = "UPDATE Object SET Location='DEATHROOM' , Available='False' , Takeable='False' WHERE Object_Id='FLASHLIGHT'"
    cur.execute(sql)
    print("What...why did it suddenly get so dark here... Where did my flashlight go..?!")

def deathByFire():
    print("Your oily clothes burn you alive. Maybe you should have considered that before lighting an oil lamp.")

def deathByTrip():
    print("Your long robes trip you up on the steep stairs and you fall snapping your neck. Maybe illuminate your way next time.")
    
def playAudio():
    pygame.mixer.music.play()

def stopAudio():
    pygame.mixer.music.stop()

db = mysql.connector.connect(host="localhost",
                           user="root",
                           passwd="MountainDiscoLadder",
                           db="covdb",
                           buffered=True)

# Initializing the music
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('TestSong.wav')
pygame.mixer.music.play()

# Initializing the emptyscreen, loading titles and resetting the location
WalkwayVoices = QuestVoices = TrophyVoices = AtticVoices = oilBody = Flashlight = firstKey = False
lightSource = True   
location = "MAINHALL" 
command = ""
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
#time.sleep(3)  
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
print("\n")
print("I can hear a whispy voice around me... I can almost make out the words...")
#time.sleep(3)
cprint("... you ever talk to animals? I find their company extremly revealing...", 'blue')
look()


# Main Loop 
# If player has no lightsource, add a line after each loop that says 'It is so dark in here'
while command!="quit" and command!="exit" and location!="THEEND":
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
    elif command=="look" or command=="l":
        look()

    # Taking objects 
    elif command=="take" or command=="get" and target!="":
        getOK = getObject(target)
        # if getOK==1:
            # if location=="SECRETROOM" and target=="ladder":
            #     takeLadder()
            # elif location=="DININGHALL" and target=="key":
            #     takeStudyKey()
            # elif location=="LIBRARY" and target=="key":
            #     takeAtticKey()
            # elif location=="FOUNTAIN" and target=="key":
            #     takeGlimmer()

    elif command=="use":
        if target=="":
            print("I don't know what to use.")
        elif location=="MAINHALL" and target=="ladder":
            useLadder()
        elif location=="HALLWAY" and target=="key" and firstKey==False:
            useStudyKey()
            firstKey=True
        elif location=="HALLWAY" and target=="key":
            useAtticKey()
        elif location=="ATTIC" and target=="switch":
            useAtticSwitch()
            location = "MAINHALL"
            look()
            print(" It seems that the switch moved the statue, revealing a door behind it...")
        elif location=="TROPHYROOM" and target=="glimmer":
            useGlimmer()
        elif location=="WELL" and target=="bucket":
            useBucket()
        else:
            print("I can't use that")
        

    # Movement 
    #TODO IS THAT QUEST B-ROOM SUPPOSED TO BE MASTER
    elif command=="north" or command=="east" or command=="south" or command=="west" or command=="n" or command=="e" or command=="s" or command=="w" \
        or command=="nw" or command=="sw" or command=="ne" or command=="se" or command=="northwest" or command=="southwest" or command=="northeast" or command=="southeast" \
        or command=="up" or command=="u" or command=="down" or command=="d":
       
        movedLocation = move(location, command)
        if location == movedLocation:
            print("I can't move there")
        else:
            location = movedLocation
            look()
        if location=="MASTERBEDROOM" and QuestVoices==False:
            eventMasterBedroomVoices()
            QuestVoices = True
        if location=="WALKWAYBATH" and WalkwayVoices==False:
            eventWalkwayVoices()
            WalkwayVoices = True
        if location=="TROPHYROOM" and TrophyVoices==False:
            eventTrophyVoices()
            TrophyVoices = True
        if location=="ATTIC" and AtticVoices==False:
            eventAtticVoices()
            AtticVoices = True
        if location=="BATHROOM" and Flashlight==False and lightSource==True:
            loseFlashlight()
            lightSource = False
        if location=="QUESTBEDROOM" and lightSource==False:
            eventQuestBedroomFall()
            oilBody = True
        if location=="ATTIC" and lightSource==False:
            deathByTrip()
            command="quit"
        if location=="ATTIC" and oilBody==True:
            deathByTrip()
            command="quit"
        if location=="HALLWAY" and lightSource==False:
            print("I can see some light coming from the Chidlren's Room.")

    #Might work, tbc
    elif command=="restart":
      db.rollback()
      command = ""
      location = "MAINHALL"
      look()
   
    # Light command
    elif command=="darkness" and location=="RIDDLEROOM":
        eventRiddleDoorOpening()

    
    elif command=="light":
        light()
        lightSource = True

    elif command=="read" and target!="":
        readObject(target)

    elif command=="eat" and target!="":
        eatObject(target)
        if target=="food":
            print("Why did you think that was fine? It's been sitting there for god knows how long!")
            command="quit"
        if target=="pillow":
            print("Yuck")
        if target=="newspaper":
            print("Enlightening!")
            print("Also slightly poisonous")
            command="quit"
        

    # Audio Commands
    elif command=="play":
        playAudio()
    
    elif command=="stop":
        stopAudio()
    
    # Unknown Command
    elif command!="quit" and command!="exit" and command!="":
        print("I don't think I can",command)
    
   

if (location=="THEEND"):
    print("You managed to make it out alive.")
    print("But your adventure is just starting.")
    print("Thank you for playing episode one of Calling of Villa! If you would like to play some more, please send as much money as you want.")
    print("Visit us at users.metropolia.fi/~oskarits/WebPage") 
else:
    print("Don't be gone too long...")
    time.sleep(3)
db.rollback()