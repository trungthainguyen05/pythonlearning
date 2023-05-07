from lib import mouseControl

linkGoogleChrome = '"C:\Program Files\Google\Chrome\Application\chrome.exe"'

while True:
    print('''
    0. Exit program
    1. Open google chrome
    2. ....
    
    ''')

    command = input('Please input your command: ')

    if command.isdigit():
        command = int(command)

        if command == 0:
            break
        elif command == 1:
            pass
