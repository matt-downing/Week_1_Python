#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


def manageAccountDetails():
    print(" ")
    print("Change an option")
    print("1. Name:", username  )
    print("2. Age:", userage )
    print("3. Location:", userlocation)
    print("4. Go back")
    input("Please choose a number: ")

def create_account(self):
        username = input("What is your name?:  ")
        userage = input("How old are you?:  ")
        userlocation = input("Where are you from?:  ")
        p1 = Person(username, userage, userlocation)
#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")       
            if 'p1' in globals() :
                username2 = input("What is your name?:  ")
                userage2 = input("How old are you?:  ")
                userlocation2 = input("Where are you from?:  ")
                p2 = Person(username2, userage2, userlocation2)
                social_network_ui.mainMenu()
            else:
                username = input("What is your name?:  ")
                userage = input("How old are you?:  ")
                userlocation = input("Where are you from?:  ")
                p1 = Person(username, userage, userlocation)
                social_network_ui.mainMenu()


        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            if input("Please type your username: ") == username:
                while True:
                    if inner_menu_choice == "5":
                        break
                    elif inner_menu_choice == "1":
                        print("1. Username: ", username)
                        print("2. Age: ", userage)
                        print("3. Location: ", userlocation)
                        print("4. Go back")
                        if input("Please choose a number: ") == "1":
                            username = input("New username: ")
                                                
                        elif input("Please choose a number: ") == "2":
                            userage = input("New age: ")
                                                
                        elif input("Please choose a number: ") == "3":
                            userlocation = input("New location: ")
                                                
                        elif input("Please choose a number: ") == "4":
                            social_network_ui.manageAccountMenu()
                            break
                        else:
                            print("Invalid Input") 
                    elif inner_menu_choice == "2":
                        friendlist = []
                        friendlist.append(input("Add a friend by username: "))
                        break
                    elif inner_menu_choice == "3":
                        print("1. ",friendlist[0])
                        print("5. Go back")
                        message_choice = input("Choose a friend to message: ")
                        if message_choice == "1":
                            messagelist = []
                            messagelist2 = []
                            messagelist2.append(input("Type your message here: "))
                        break
                    elif inner_menu_choice == "4":
                        print (messagelist)
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()
            elif input ("Please type your username: ") == username2:
                while True:
                    if inner_menu_choice == "5":
                        break
                    elif inner_menu_choice == "1":
                        print("1. Username: ", username2)
                        print("2. Age: ", userage2)
                        print("3. Location: ", userlocation2)
                        print("4. Go back")
                        if input("Please choose a number: ") == "1":
                            username2 = input("New username: ")
                                                
                        elif input("Please choose a number: ") == "2":
                            userage2 = input("New age: ")
                                                
                        elif input("Please choose a number: ") == "3":
                            userlocation2 = input("New location: ")
                                                
                        elif input("Please choose a number: ") == "4":
                            social_network_ui.manageAccountMenu()
                            break
                        else:
                            print("Invalid Input") 
                    elif inner_menu_choice == "2":
                        friendlist2 = []
                        friendlist2.append(input("Add a friend by username: "))
                        break
                    elif inner_menu_choice == "3":
                        print("1. ",friendlist2[0])
                        print("5. Go back")
                        message_choice = input("Choose a friend to message: ")
                        if message_choice == "1":
                            messagelist = []
                            messagelist.append(input("Type your message here: "))
                        break
                    elif inner_menu_choice == "4":
                        print (messagelist2)
                        break
                    else:
                        inner_menu_choice = social_network_ui.manageAccountMenu()



        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
