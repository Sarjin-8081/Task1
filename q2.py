game=input("Welcome to Treasure Land\nchoose direction:-\n1.right\n2.left\n=")
if game=="right":
    print("Game Over.")
elif game=="left":
    game_2=input("Do you want to swim or wait\n=")
    if game_2=="swim":
        print("Game Over.")
    elif game_2=="wait":
        game_3=input("Choose a color\n1.red\n2.blue\n3.yellow\n=")
        if game_3=="blue" or game_3=="red":
            print("Game Over.")
        elif game_3=="yellow":
            print("You Win.")
        else:
            print("Invalid Direction")