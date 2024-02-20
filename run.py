def run_game():
    """
    Display the Welcome message and Menu Options and 
    request user to choose a Menu Option.
    """
    print("##################")
    print("Welcome to Hangman")
    print("##################\n")
    print("Menu Options:")
    print("1. Play Game")
    print("2. Rules")
    print("3. Exit Game\n")
    print("Please choose a Menu Option")

    menu_option = input("Enter 1, 2 or 3\n")
    validate_input(menu_option)

    # if menu_option == 1:
    #     play_game()
    # elif menu_option == 2:
    #     display_rules()
    # elif menu_option == 3:
    #     exit()

def validate_input(choice):
    """
    Check the user's input to ensure they enter a correct Menu option.
    """
    try:
        int_choice = int(choice)
        if int_choice == 1:
            play_game()
    
    except ValueError:
        print(f"Invalid data entered. Please choose a Menu Option.\n")
            

def play_game():
    """
    Displays the empty spaces for the word.
    Displays the images.
    """
    print("Hello World.")
    print("_ _ _ _ _")

run_game()