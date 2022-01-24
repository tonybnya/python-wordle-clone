import random
import sys
from threading import Thread, Timer, Lock
import time
from datetime import datetime
import colorama
from colorama import Fore, Back, Style
from progress.bar import Bar

colorama.init(autoreset=True)


def load_progress_bar():
    """
    Function to simulate a progress bar.
    """

    progress_bar = Bar("Loading...", fill=BAR, suffix="%(percent)d%%")

    for _ in range(100):
        time.sleep(0.02)
        progress_bar.next()

    progress_bar.finish()
    time.sleep(1)


def load_words(filename):
    """
    Function to load words from the dictionary text file.
    """

    with open(filename) as file_obj:
        lines = file_obj.readlines()
        words = [word.strip() for word in lines]

    return words


def random_word(words):
    """
    Function to pick a random word from the dictionary list file.
    """

    word_to_guess = random.choice(words)

    return word_to_guess


def quicksort(words):
    """
    Function to the common Quicksort Algorithm,
    to sort the list of words alphabetically.
    """

    if len(words) <= 1:
        return words

    pivot = words[0]
    less, greater = [], []

    for word in words[1:]:
        if word <= pivot:
            less.append(word)
        else:
            greater.append(word)

    return quicksort(less) + [pivot] + quicksort(greater)


def get_input(words):
    """
    Function to get the input form the user.
    """

    print()
    guess = input("Enter your guess > ").upper()

    if len(guess) != 5 or not guess.isalpha():
        print("Your guess must be 5 letters!")
    elif guess not in words:
        print("Your guess is not in our dictionary!")
    else:
        return guess


def color_on_your_guess(guess, word_to_guess):
    """
    Function to colored the spot of the letters in the input word.
    """

    green = Back.GREEN
    yellow = Back.YELLOW
    grey = Back.LIGHTBLACK_EX

    colors = [grey] * 5

    # GREEN
    # If any letter in your guess is in word_to_guess and in the right place,
    # this letter color is green
    for i in range(len(guess)):
        if guess[i] == word_to_guess[i]:
            colors[i] = green

    # YELLOW
    # If any letter in your guess is in word_to_guess and in the wrong place,
    # this letter color is yellow
    for i in range(len(guess)):
        if guess[i] in word_to_guess and guess[i] != word_to_guess[i]:
            colors[i] = yellow

    # GREY
    # If any letter in your guess is not in word_to_guess,
    # this letter color is grey
    for i in range(len(guess)):
        if guess[i] not in word_to_guess:
            colors[i] = grey

    for i, letter in enumerate(guess):
        print(colors[i] + letter, end=' ')
        # print(colors[i] + Style.BRIGHT + letter, end=' ')


def timer():
    """
    Function to show a clock.
    """

    while True:
        now = datetime.now()
        print(
            Fore.RED + now.strftime("%a, %b %d %Y, %H:%M:%S"),
            end="\r",
            flush=True
        )

        time.sleep(1)


# The standard boilerplate statement to call the main program.
if __name__ == "__main__":
    FORMAT1 = Style.BRIGHT + Fore.GREEN
    FORMAT2 = Style.BRIGHT + Fore.RED
    GITHUB = "https://github.com/tonybnya"
    BAR = Style.BRIGHT + Fore.GREEN + chr(9679)  # chr(9679) == '●'

    time.sleep(.2)
    print()
    time.sleep(.2)

    print(FORMAT1 + "WORDLE - The Word Trending Game.")
    time.sleep(.2)
    print(FORMAT1 + "A CLI version builded by tonybnya.")
    time.sleep(.2)
    print(FORMAT1 + f"Github: {GITHUB}\n")
    time.sleep(.2)

    with open("howto.txt") as f:
        time.sleep(.2)
        print(f.read())

    time.sleep(2)
    load_progress_bar()
    time.sleep(.2)
    print(FORMAT2 + "Go!")
    time.sleep(.2)

    filename = "words.txt"
    words = load_words(filename)
    words = quicksort(words)
    word_to_guess = random_word(words)

    with open("response.txt", "w") as file_obj:
        file_obj.write(word_to_guess)

    # TODO : Handle Exceptions

    counter = 0
    while True:
        guess = get_input(words)
        counter += 1
        print(f"{counter}/6 tries...")

        color_on_your_guess(guess, word_to_guess)

        if guess == word_to_guess:
            print(f"\nYou win in {counter}/6 tries.")
            break

        if counter == 6:
            print(f"\n{counter} tries completed.")
            print("Game Over!")
            break
