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

    while True:
        menu_option = input("Enter 1, 2 or 3\n")
        if menu_option not in ("1","2","3"):
            print("Invalid data entered. Please choose a Menu Option.\n.")
        else:
            break

    if menu_option == "1":
        play_game()
    elif menu_option == "2":
        display_rules()
    elif menu_option == "3":
        quit()


def display_rules():
    """
    Prints the rules of the game.
    """
    print('''
    The Rules of the game are:\n
    1. A word will be picked at random.
    2. An underscore will be displayed for each letter in the word.
    3. You will have 6 chances to guess every letter in the word.
    4. When you get a letter correct it will replace the underscore.
    5. When you get a letter incorrect a line will be added to the man.
    6. The game is over when you get all the letters correct or
       the image of the man is complete.
          ''')
    play_game()

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
    print(word_to_print) # Delete this line


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

