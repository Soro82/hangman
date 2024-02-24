import random


# The Hangman Pictures were copied from 
# https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
HANGMANPICS = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
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
  |   |
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
      |
      |
      |
      |
=========''']

# Global Variables to use in multiple functions.
blank_word = []

def run_game():
    """
    Display the Welcome message and Menu Options and 
    request the user to enter their name.
    """
    print("##################")
    print("Welcome to Hangman")
    print("##################\n")

    #user_name = get_user_name()

    print("Menu Options:")
    print("1. Play Game")
    print("2. Rules")
    print("3. Exit Game\n")
    #print(f"{user_name} Please choose a Menu Option.")

    get_user_option()


def get_user_option():
    """
    Ask the user to choose a menu option and called the required function.
    """
    blank_word.clear()
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


def get_user_name():
    """
    Ask the user to enter their name.
    Validate the name and return it.
    """
    while True:
        name = input("Please enter your name\n").capitalize()

        if name.isalpha() and len(name) > 1:
            return name
        else:
            print("Your name must only contain letters")
            print("and contain at least 2 letters.\n")


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
    print("Please choose a Menu Option.")
    get_user_option()

def pick_random_word():
    """
    Generate a random number and pick a random word from the words list.
    """
    words = ["horse", "donkey", "camel", "monkey", "mouse"]
    word_num = random.randint(0,4)
    random_word = words[word_num]
    return random_word


def print_blank_word(word_to_print):
    """
    Print a list of underscores for each letter in the word picked.
    """
    word_length = len(word_to_print)

    for letter in range(word_length):
        blank_word.append("_ ")

    print(*blank_word)
    print(word_to_print) # Delete this line


def ask_for_answer():
    """
    Ask the user for their answer.
    Validate the answer given.
    Check if the answer is correct.
    """
    while True:
        answer = input("Please choose a letter\n").lower()

        if answer.isalpha() and len(answer) == 1:
            return answer
        else:
            print("Invalid entry. Please choose a single letter.\n")


def play_game():
    """
    Displays the empty spaces for the word.
    Displays the images.
    """
    word_picked = pick_random_word()
    print_blank_word(word_picked)

    lives = 6
    prev_answers = []
    while lives > 0:
        print(f"You have {lives} lives left.")
        answer = ask_for_answer()
        if answer in prev_answers:
            print("YOu have already tried this letter.")
        else:
            prev_answers.append(answer)     
            if answer in word_picked:
                answer_index = word_picked.index(answer)
                blank_word[answer_index] = answer + " "
                print(*blank_word)
                print("Correct. Good guess.\n")

                # Check if word is complete.            
                if "_ " not in blank_word:
                    print("Congratulations. You won the game.")
                    print("Why not try again.\n")
                    get_user_option()
                    
            else:
                print("Incorrect")
                print(HANGMANPICS[lives])
                print(*blank_word)
                lives -=1
                if lives == 0:
                    print("Game over. Why not try again.\n")
                    get_user_option()
        

    
run_game()

