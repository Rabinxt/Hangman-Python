from word import words
import random
import string

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)  # set of the 26 letters
    used_letters = set()  # used letters set is initialized fresh each time
    lives = 6

    print("Welcome to hangman game!!")

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print('You have used these letters:',' '.join(used_letters),f"and {lives} lives remaning")
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word:", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Letter is not in the list! ")
                lives = lives-1
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')
            lives = lives -1

    if lives ==0:
        print(f"You died , Correct word is {word}")
    else :
        print(f"You have guessed {word} correctly")

hangman()