import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'watermelon',
             'elephant', 'tiger', 'giraffe', 'lion', 'zebra', 'cheetah',
             'python', 'java', 'javascript', 'ruby', 'php', 'html', 'css',
             'football', 'basketball', 'soccer', 'tennis', 'volleyball', 'cricket',
             'mountain', 'ocean', 'forest', 'desert', 'river','youtube']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word!")

    while True:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            attempts -= 1
            print("Wrong guess!")
            print(f"Attempts left: {attempts}")
            if attempts == 0:
                print("Game Over! You ran out of attempts.")
                print(f"The word was: {word}")
                break
        
        if all(letter in guessed_letters for letter in word):
            print(display_word(word, guessed_letters))
            print("Congratulations! You guessed the word!")
            break

hangman()
