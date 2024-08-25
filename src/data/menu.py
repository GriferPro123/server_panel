import os
while True:
    os.system('cls')
    print("  ______________ ")
    print(" / Server panel \ ")
    print(" \______________/ ")
    print("")
    print("1. Settings")
    print("2. Start server")
    print("3. Exit")
    f = input()
    if f == "1":
        os.system('cls')
        print("  __________ ")
        print(" / Settings \ ")
        print(" \__________/ ")
        print("")
        print("1. Server ip")
        print("2. Server port")
        print("3. Exit to main menu")
        v = input()
        if v == "1":
            os.system("cls")
            os.system("data\setting.bat")
        elif v == "2":
            os.system("cls")
            os.system("data\setting2.bat")
    elif f == "2":
        os.system("cls")
        os.system("data\server.bat")
    elif f == "3":
        exit()
