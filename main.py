import menu
import simplePop

if __name__ == '__main__':
    # Sets Menu Choice to 1
    choice = 1

    # Menu loop
    while choice != 0 :
        choice = menu.mainMenu()

        # Choices
        # 0. Quit
        # 1. Simple All known
        # 2. Finding r
        if choice == 1:
            population = simplePop.allKnownCase()
            print(str(population))
        elif choice == 2:
            r = simplePop.findrval()
            print(str(r))




