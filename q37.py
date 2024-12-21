print("Welcome to the Pirate Island")
choice1 = input("Do you want to go 'left' or 'right'? ").lower()
if choice1 == "right":
    print("Game Over\n")
elif choice1 == "left":
    choice2 = input("Do you want to 'dig for treasure' or 'sail the ship'? ").lower()
    if choice2 == "dig for treasure":
        print("Game Over\n")
    elif choice2 == "sail the ship":
        choice3 = input("Choose between 'shark', 'pirate ship', or 'mermaid': ").lower()
        if choice3 in ["shark", "pirate ship"]:
            print("Game Over\n")
        elif choice3 == "mermaid":
            print("You Win\n")