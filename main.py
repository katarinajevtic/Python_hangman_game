import random


def chose_word():
    words = ["python", "hangman", "coding", "challenge", "luck", "book", "chair", "mouse", "sunshine", "rain"]
    return random.choice(words)


def display_words(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman_game():
    name = input("Please enter your name: ").upper()
    print(f"Hi {name}! Welcome to Hangman!")

    words_guesses = chose_word()
    guessed_letter = []
    incorrect_guesses = 0
    guess_attempts = 10

    while incorrect_guesses <= guess_attempts:
        current_display = display_words(words_guesses, guessed_letter)
        print("Current word: ", current_display)

        guess = input("Guess a letter: ").lower()

        if guess.isalnum() and len(guess) == 1:
            if guess in guessed_letter:
                print("You already guessed that letter, try again")
            elif guess in words_guesses:
                guessed_letter.append(guess)
                print("Good guess!")
            else:
                incorrect_guesses += 1
                print("Incorrect guess! Attempts left: ", guess_attempts - incorrect_guesses)
        else:
            print("Invalid input. Please enter a single letter.")

        if set(guessed_letter) == set(words_guesses):
            print("Congratulation! You guessed a word: ", words_guesses)
            break
        if incorrect_guesses == guess_attempts:
            print("Sorry, you ran out of attempts. The word was:", words_guesses)


if __name__ == '__main__':
    hangman_game()
