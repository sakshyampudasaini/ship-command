command = ""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("The ship is already started")
        else:
            started = True
            print("The ship starts")
    elif command == "stop":
        if not started:
            print("The ship is already stopped")
        else:
            started = False
            print("The ship stops")
    elif command == "help":
        print("""
start = starts the ship
stop = stops the ship
quit = the game quits
""")
    elif command == "quit":
        print("Play again next time")
        break
    else:
        print(f"Sorry, but I didn't get you.")
