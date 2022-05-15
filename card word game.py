start = False
stop = True
while True:
    user_input = input(">")
    if user_input == "start":
        if start:
            print("car is already started")
        else:
            start = True
            stop = False
            print("car is started")
    elif user_input == "stop":
        if stop:
            print("car is already stopped")
        else:
            start = False
            stop = True
            print("car is stopped")
    elif user_input== "help":
        print('''
start = car will start,
stop = car will stop,
quit = stop
        ''')
    elif user_input=="quit":
        print("bye")
        break
    else:
        print("I dont understand what you are telling")
