import random

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


def validate_input(choice):
    """
    Check the user's input to ensure they enter a correct Menu option.
    """
    try:
        int_choice = int(choice)
        if int_choice == 1:
            play_game()
        # elif menu_option == 2:
        #     display_rules()
        elif int_choice == 3:
             quit()
        else:
            print("Invalid data entered. Please choose a Menu Option.")
            run_game()
    
    except ValueError:
        print(f"Invalid data entered. Please enter a number.\n")
           

def play_game():
    """
    Displays the empty spaces for the word.
    Displays the images.
    """
    word_num = random.randint(0,10)
    print(word_num)
    print("Hello World.")
    
    
run_game()