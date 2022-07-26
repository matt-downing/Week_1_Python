# You can implement user interface functions here.



def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")

def manageAccountp1():
    if input("Please choose a number: ") == "1":
        username = input("New username: ")
                            
    elif input("Please choose a number: ") == "2":
        userage = input("New age: ")
                            
    elif input("Please choose a number: ") == "3":
        userlocation = input("New location: ")
                            
    elif input("Please choose a number: ") == "4":
        manageAccountMenu()
    else:
        print("Invalid Input") 