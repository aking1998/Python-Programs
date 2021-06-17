
command=''
started = False
stopped = False
while command !="quit":
    command = input(">>>>")
    if command=="start":
        
        if started:
            print("Car Started Already..")
        else:
            print("Car Started..")
        started = True

    elif command=="stop":

        if stopped:
            print("Car Stopped Already..")
        else:
            print("Car Stopped..")
        stopped = True

    elif command=="help":
        print("Rules of the Game-")
        print("Enter 'start' command to start the car")
        print("Enter 'stop' command to stop the car")
        print("Enter 'quit' command to exit the game")

    elif command=="quit":
        print("GAME END!!")
        
    else:
        print("I don't understand the command..")
        
        
        
        
    