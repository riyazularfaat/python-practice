command = ""
is_started = False
is_stopped = False
while True:
    command = input("> ").lower()
    if command == "help":
        print('''
start -> to start the car
stop -> to stop the car
help -> to get help
quit -> to quit 
        ''')
    elif command == "start":
        if is_started:
            print("The car has alread started.")
        else:
            is_started = True
            print("The car starts.")
    elif command == "stop":
        if is_stopped:
            print("The car has already stopped.")
        else:
            is_stopped = True
            print("The car stops.")
    elif command == "quit":
        break
    else:
        print("Invalid choice....")
            
     
        