#######-####### Main Menu #######-#######
def mainMenu():
    #Menu Options
    print("Please Select your option below:")
    print("1. Simple All Known")
    print("2. Simple Find Population Rate")
    print("0. Quit")

    # Gather user input
    user_option = int(input())
    print("you picked " + str(user_option))

    # Return option
    return user_option
