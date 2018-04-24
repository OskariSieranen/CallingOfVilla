import mysql.connector

# Commands go here | First person always. Ex. "I have *List of items*"

# Connection here

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