import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

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
    print("Please choose a Menu Option.")

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
    """
    Generate a random number and pick a random word from the words list.
    """
    words = ["horse", "donkey", "chicken", "monkey", "mouse"]
    word_num = random.randint(0,4)
    random_word = words[word_num]
    return random_word


def print_blank_word(word_to_print):
    """
    Print a list of underscores for each letter in the word picked.
    """
    blank_word = ""
    word_length = len(word_to_print)

    for word in range(word_length):
        blank_word = blank_word+"_ "

    print(blank_word)
    print(word_to_print)


def ask_for_answer(word):
    """
    Ask the user for their answer.
    Validate the answer given.
    Check if the answer is correct.
    """
    answer = input("Please choose a letter\n")
    print(answer)
    check_answer(answer, word)


def check_answer(user_answer, ran_word):
    """
    Check if the letter chosen by the user is in the word.
    """
    if user_answer in ran_word:
        print("Correct")
    else:
        print("Incorrect")


def play_game():
    """
    Displays the empty spaces for the word.
    Displays the images.
    """
    word_picked = pick_random_word()
    print_blank_word(word_picked)
    print_images(3)
    ask_for_answer(word_picked)
        
    
def print_images(i):
    """
    Print image for current state of game.
    """
    print(HANGMANPICS[i])

    
run_game()

