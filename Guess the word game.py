import random

# List of random words related to Pakistan
words = [
    "lahore", "karachi", "islamabad", "quaid", "pakistan", "khyber", "faisal", 
    "punjab", "sindh", "peshawar", "multan", "balochistan", "rawalpindi", 
    "freedom", "tigers", "mountain", "desert", "culture", "tea", "cricket", 
    "mughal", "badshahi", "fort", "indus", "pakistani", "sufi", "shawarma", 
    "chapli", "biryani", "karahi", "lahori", "mohammad", "sindhi", "mullah", 
    "shahbaz", "gilgit", "hunza", "karakoram", "swat", "faisalabad", "shahjahan"
]

# Function to choose a random word
def choose_word():
    return random.choice(words)

# Function to display the current state of the word with underscores
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Guess the word game function
def guesstheword():
    print("Welcome to the guess the word Game!")
    print("All words are related to Pakistan.")
    
    word = choose_word()  # Random word from list
    guessed_letters = set()  # Store guessed letters
    incorrect_guesses = set()  # Store incorrect guesses
    attempts = 6  # Number of attempts allowed
    
    while attempts > 0:
        # Display current state of the word
        print("\nCurrent word: ", display_word(word, guessed_letters))
        print("Incorrect guesses: ", ' '.join(incorrect_guesses))
        print(f"Remaining attempts: {attempts}")
        
        # Take a guess from the player
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter.")
            continue

        # Check if the guess is correct
        if guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses.add(guess)
            attempts -= 1
            print("Wrong guess!")

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations, you guessed the word:", word)
            break
    
    # If attempts run out, game over
    if attempts == 0:
        print("\nGame Over! The word was:", word)

# Run the game
guesstheword()