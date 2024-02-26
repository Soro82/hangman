# Hangman

Click [here](https://hangman-soro82-05b97f95a765.herokuapp.com) for the live link.

## Introduction

The Hangman game is a Python command-line project. It is written in Python and deployed using Heroku. A word is picked at random and the user has seven chances to guess the correct letters in the word. The word is displayed with an underscore in place of each letter in the word.If the user guesses a correct letter, the underscore for that letter is replaced with the letter. If the user guesses an incorrect letter, the next image of the hangman is displayed and the user is told how many lives they have left. 


## Table of Contents

* [User Stories](#user-stories)
* [Flowcharts](#flowcharts)
   * [Run Game](#run-game)
   * [Get User's Answer](#get-users-answer)
   * [Play Game](#play-game)
* [Features](#features)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Stories

As a user I want to be able to:

* enter my name before I start the game.
* choose from a list of options.
* start the game.
* see the rules of the game.
* Exit the game.
* know how many letters are in the word to guess.
* know how many lives I have left after each guess.
* be told when I get an answer correct.
* see my correct answers in their correct position in the word.
* be told when I get an answer incorrect.
* see an image of the hangman after each incorrect answer.
* be told when I correctly guessed all the letters in the word.
* know if I previously guessed the letter.
* know when the game is over.
* to choose to play again or exit the game.

[Back to Top](#hangman)

## Flowcharts

I used [Lucidchart](https://www.lucidchart.com/pages/) to create the flowcharts for my game. I found them really helpful in planning what functions I need for the game to work in the way that I wanted it to.

### Run Game

I created my first flowchart to plan out the basic operations of the game.

* Display the welcome message and menu options.
* Ask the user to choose a menu option.
* Validate the user's input.
* what each menu option does.

![Run Game Flowchart](documentation/flowcharts/run_game.png)

[Back to Top](#hangman)

### Get User's Answer

Next I created a flowchart to plan how to get the answer from the user and what to do with it.

* Ask the user to choose a letter.
* Check if the user has entered a letter.
* Inform the user if they did not enter a single letter.
* If the user enters a valid input, check if the answer is correct.
* If it's incorrect, display the next hangman image.
* If it's correct, find the index of the user's answer.
* Display the word with the user's answer in it.

![Get User's Answer Flowchart](documentation/flowcharts/get_user_answer.png)

[Back to Top](#hangman)

### Play Game

At first I had a separate function to check the user's answer but I realized that I needed to do it in the same function that loops through the game so I created the play_game flowchart. Here I:

* Print the word in question.
* Ask the user to choose a letter.
* Validate the input.
* Check if the letter was asked previously.
* Display the images.

![Play Game Flowchart](documentation/flowcharts/play_game.png)

[Back to Top](#hangman)

## Features

### Get User's Name

* Ask the user to enter their name.
* Inform the user if they enter and invalid entry.

![Get User's Name Screeshot](documentation/screenshots/username_validation.png)

### Menu Options

* Display Menu Options.
* Display the User's Name.
* Ask the user to choose a menu option.

![Menu Options Screenshot](documentation/screenshots/menu_options.png)

* Validate the Menu Option chosen by the user.

![Menu Options Validation Screenshot](documentation/screenshots/menu_options_validation.png)

### Display Rules

![Display Rules Screenshot](documentation/screenshots/display_rules.png)

### Start Game

* Display underscores for each letter in the word.
* Display the number of lives the user has left.

![Display underscores Screenshot](documentation/screenshots/blank_word_and_lives.png)

<details>
<summary>### User Answers</summary>

* Answer Validation

![Answer Validation Screenshot](documentation/screenshots/answer_validation.png)

* First Correct Answer

![First Correct Answer Screenshot](documentation/screenshots/first_correct_answer.png)

* Answer Tried Previously

![Answer Tried Previously Screenshot](documentation/screenshots/previous_answer.png)

* Second Correct Answer

![Second Correct Answer Screenshot](documentation/screenshots/second_correct_answer.png)
</details>

<details>
<summary>### Incorrect Answers</summary>

* First Incorrect Answer

![First Incorrect Answer](documentation/screenshots/incorrect_answers/first_incorrect_answer.png)

* Second Incorrect Answer

![Second Incorrect Answer](documentation/screenshots/incorrect_answers/second_incorrect_answer.png)

* Third Incorrect Answer

![Third Incorrect Answer](documentation/screenshots/incorrect_answers/third_incorrect_answer.png)

* Fourth Incorrect Answer

![Fourth Incorrect Answer](documentation/screenshots/incorrect_answers/fourth_incorrect_answer.png)

* Fifth Incorrect Answer

![Fifth Incorrect Answer](documentation/screenshots/incorrect_answers/fifth_incorrect_answer.png)

* Sixth Incorrect Answer

![Sixth Incorrect Answer](documentation/screenshots/incorrect_answers/sixth_incorrect_answer.png)

</details>

### Game Over

* Final Correct Answer

![Final Correct Answer Screenshot](documentation/screenshots/final_correct_answer.png)

* Final Incorrect Answer

![Final Incorrect Answer Screenshot](documentation/screenshots/incorrect_answers/last_incorrect_answer.png)

