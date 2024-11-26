import random
words = ["apple", "banana", "grape", "orange", "kiwi"]

def scramble_word(word):
    word_list = list(word)  
    random.shuffle(word_list)  
    return ''.join(word_list)

def word_scramble_game():
    original_word = random.choice(words)
    scrambled_word = scramble_word(original_word)
    
    print("Welcome to the Word Scramble Game!")
    print(f"Try to guess the original word from the scrambled word: {scrambled_word}")
    
    attempts = 5
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left. Enter your guess: ").strip()

        if not guess:
            print("Invalid input! Please enter a non-empty guess.")
            continue

        if guess.lower() == original_word.lower():
            print("Congratulations! You guessed the word correctly.")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect guess. You have {attempts} attempts remaining.")
            else:
                print(f"Sorry, you've run out of attempts. The original word was: {original_word}")

word_scramble_game()
