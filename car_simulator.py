
command = ""
is_started = False
is_stopped = False
while command != "quit":
    command = input("> ").lower()
    if command == "help":
        print('''
start = to start the car
stop = to stop the car
quit = to exit
''')
    elif command == "start":
        if is_started:
            print("Car is already started.")
        else:
            is_started = True
        print("Car has started....Ready to go.")
    elif command == "stop":
        if is_stopped:
            print("Car is already stopped.")
        else:
            print("Car has stopped.")
    else:
        print("Sorry, I don't understand that. Please enter a valid command.")
        
    