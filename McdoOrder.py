def Order():
    Order = []
    Menu = []
    print("Welcome to Mcdonald's!")
    ChoiceMenu = input("Would you like to order a menu? Y/N")
    if ChoiceMenu == "Y":
        Burger = input("Which Burger do you want? (BigMac/Cheeseburger)")
        if Burger == "CheeseBurger":
            ExtraCheese = input("Add Extra Cheese?")
            if ExtraCheese == "Y":
                Menu.append("ExtraCheese")
            ExtraBacon = input("Add Extra Bacon?")


