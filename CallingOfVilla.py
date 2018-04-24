# Tabs: 4 spaces

import mysql.connector

# Commands go here | First person always. Ex. "I have *List of items*"

def inventory():
    cur = db.cursor()
    sql = "SELECT ObjectId, Description FROM Object"
    cur.execute(sql)
    if cur.rowcount()>=1:
        print("I have: ")
        for item in cur.fetchall():
            print("-" + row[0])
    else:
        print("I don't have anything at the moment.")
    return

# Connection here
db = mysql.connector.connect(host="localhost",
                            user="",
                            passwd="",
                            db="CallingOfVilla",
                            buffered=True)

                            
# Initializing the location and an empty screen

# Main Loop
while command != "quit" and location !=  : # Name of end screen

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