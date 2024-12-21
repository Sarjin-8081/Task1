print("Welcome to the Magic Forest")
choice1 = input("Do you want to go 'north' or 'south'? ").lower()
if choice1 == "south":
    print("Game Over\n")
elif choice1 == "north":
    choice2 = input("Do you want to 'cross the river' or 'follow the path'? ").lower()
    if choice2 == "cross the river":
        print("Game Over\n")
    elif choice2 == "follow the path":
        choice3 = input("Choose between 'fairy', 'ogre', or 'elf': ").lower()
        if choice3 in ["fairy", "ogre"]:
            print("Game Over\n")
        elif choice3 == "elf":
            print("You Win\n")