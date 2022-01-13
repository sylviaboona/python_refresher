command = ''
started = False
# while true - the program executes until it breaks
while True: 
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('Car is already started...')
        else:
            started = True
            print('Car started')
    elif command == 'stop':
        if not started:
            print('Car is already stopped...')
        else:
            started = False
            print('Car stopped')
    elif command == 'help':
        print("""
    start - to start car
    stop - to stop car
    quit - to quit game
        """)
    elif command == 'quit':
        break
    else:
        print('Sorry, what was that!!')
