import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            if set(word) == set(guessed_letters):
                print("Congratulations! You guessed the word:", word)
                break
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess.")
            if attempts == 0:
                print("You ran out of attempts! The word was:", word)
                break

hangman()
