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
        # else:
         #     print("Invalid data entered. Please choose a Menu Option.")
         #     run_game()
        
    except ValueError:
        print("Invalid data entered. Please choose a Menu Option.\n")
                   

def pick_random_word():
    words = ["horse", "donkey", "chicken", "monkey", "mouse"]
    word_num = random.randint(0,4)
    random_word = words[word_num]
    return random_word


def play_game():
    """
    Displays the empty spaces for the word.
    Displays the images.
    """
    word_picked = pick_random_word()
    word_length = len(word_picked)
    print(word_picked)
    print(word_length)
    print("Hello World.")
    




run_game()