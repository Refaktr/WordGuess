import random
import os
import sys

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words(count):
    try:
        file_path = get_resource_path(f"{count}.txt")
        with open(file_path) as f:
            words = [line.strip() for line in f]
            if not words:
                print(f"❌ Error: {count}.txt is empty!")
                input("Press Enter to return to menu...")
                return None
            return words
    except FileNotFoundError:
        print(f"❌ Error: {count}.txt file not found!")
        print("Please make sure the word list file exists.")
        input("Press Enter to return to menu...")
        return None
    except Exception as e:
        print(f"❌ Error loading {count}.txt: {e}")
        input("Press Enter to return to menu...")
        return None

class LetterTracker:
    def __init__(self):
        self.correct = set()     # Green letters (correct position)
        self.present = set()     # Yellow letters (wrong position)
        self.absent = set()      # Red letters (not in word)
    
    def update(self, letter, status):
        if status == "correct":
            self.correct.add(letter.upper())
            # Remove from other sets if it was there
            self.present.discard(letter.upper())
            self.absent.discard(letter.upper())
        elif status == "present":
            if letter.upper() not in self.correct:
                self.present.add(letter.upper())
                self.absent.discard(letter.upper())
        elif status == "absent":
            if letter.upper() not in self.correct and letter.upper() not in self.present:
                self.absent.add(letter.upper())
    
    def display_alphabet(self):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("\n" + "="*50)
        print("ALPHABET STATUS:")
        print("="*50)
        
        # Display in rows of 10, 9, 7 letters (cleaner layout)
        rows = [alphabet[0:10], alphabet[10:19], alphabet[19:26]]
        
        for i, row in enumerate(rows):
            # Center alignment for each row
            if i == 1:
                print(" " * 2, end="")  # Indent second row
            elif i == 2:
                print(" " * 6, end="")  # Indent third row more
                
            for letter in row:
                if letter in self.correct:
                    print(f"\033[42m\033[30m {letter} \033[0m", end="")  # Green background, black text
                elif letter in self.present:
                    print(f"\033[43m\033[30m {letter} \033[0m", end="")  # Yellow background, black text
                elif letter in self.absent:
                    print(f"\033[41m\033[30m {letter} \033[0m", end="")  # Red background, black text
                else:
                    print(f"\033[47m\033[30m {letter} \033[0m", end="")  # White background, black text
            print()
        
        print("="*50)
        print("🟩 Correct | 🟨 Wrong position | 🟥 Not in word | ⬜ Not guessed")
        print("="*50)

def process_guess(guess_word, correct_word, letter_tracker):
    """Process a guess and update the letter tracker, return colored version"""
    # Convert both to lowercase for comparison
    guess_word = guess_word.lower()
    correct_word = correct_word.lower()
    
    correct_letters = list(correct_word)  # Make a copy to track used letters
    colors = [""] * len(guess_word)  # Store colors for each position
    
    # First pass: mark correct positions (green)
    for i, letter in enumerate(guess_word):
        if letter == correct_word[i]:
            colors[i] = "\033[42m\033[30m " + letter.upper() + " \033[0m"  # Green background
            correct_letters[i] = None  # Mark this letter as used
            letter_tracker.update(letter, "correct")
    
    # Second pass: mark wrong positions (yellow) or not in word (red)
    for i, letter in enumerate(guess_word):
        if colors[i] == "":  # Only process if not already colored green
            if letter in correct_letters:
                colors[i] = "\033[43m\033[30m " + letter.upper() + " \033[0m"  # Yellow background
                correct_letters[correct_letters.index(letter)] = None  # Mark as used
                letter_tracker.update(letter, "present")
            else:
                colors[i] = "\033[41m\033[37m " + letter.upper() + " \033[0m"  # Red background
                letter_tracker.update(letter, "absent")
    
    return "".join(colors)
    

def menu():
    clear_screen()
    print("\n" + "="*50)
    print("🎮 WELCOME TO WORDGUESS! 🎮")
    print("="*50)
    print("1. Easy Game (4-letter words)")
    print("2. Medium Game (5-letter words)")
    print("3. Hard Game (6-letter words)")
    print("4. Exit")
    print("="*50)
    choice = input("Choose an option: ")

    if choice == "1":
        words = load_words(4)
        if words is None:
            return menu()
        return words
    elif choice == "2":
        words = load_words(5)
        if words is None:
            return menu()
        return words
    elif choice == "3":
        words = load_words(6)
        if words is None:
            return menu()
        return words
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        return menu()

def game_loop():
    words = menu()
    correct_word = random.choice(words)
    letter_tracker = LetterTracker()
    
    # Create a set of valid words for faster lookup
    valid_words = set(word.lower() for word in words)
    
    guess_count = 0
    max_guesses = 6
    colored_guesses = []
    
    while guess_count < max_guesses:
        # Clear screen and show fresh game state
        clear_screen()
        
        print(f"\n🎯 Guess the {len(correct_word)}-letter word!")
        print("Good luck! 🍀")
        print(f"Guess {guess_count + 1}/{max_guesses}")
        
        # Display the alphabet status at the top (FIXED POSITION)
        letter_tracker.display_alphabet()
        
        # Show ALL previous guesses BELOW the alphabet
        if colored_guesses:
            print("\nYOUR GUESSES:")
            print("-" * 30)
            for i, colored_guess in enumerate(colored_guesses):
                print(f"  {i+1}. {colored_guess}")
            print("-" * 30)
        else:
            print("\nYOUR GUESSES:")
            print("-" * 30)
            print("  (No guesses yet)")
            print("-" * 30)
        
        guess_word = input("\nEnter your guess: ").lower()
        
        if len(guess_word) != len(correct_word):
            print(f"❌ Please enter a {len(correct_word)}-letter word!")
            input("Press Enter to continue...")
            continue
            
        if not guess_word.isalpha():
            print("❌ Please enter only letters!")
            input("Press Enter to continue...")
            continue
        
        # Check if the word is in the valid word list
        if guess_word not in valid_words:
            print(f"❌ '{guess_word.upper()}' is not a valid word in our dictionary!")
            print("Please try a different word.")
            input("Press Enter to continue...")
            continue
            
        guess_count += 1
        
        # Process the guess and get colored version
        colored_guess = process_guess(guess_word, correct_word, letter_tracker)
        colored_guesses.append(colored_guess)
        
        if guess_word.lower() == correct_word.lower():
            # Clear screen and show final state
            clear_screen()
            print(f"\n🎯 Guess the {len(correct_word)}-letter word!")
            print("🎉 CONGRATULATIONS! 🎉")
            print(f"You won in {guess_count}/{max_guesses} guesses!")
            
            # Show final alphabet state
            letter_tracker.display_alphabet()
            
            # Show ALL guesses including the winning one
            print("\nYOUR GUESSES:")
            print("-" * 30)
            for i, colored_guess in enumerate(colored_guesses):
                print(f"  {i+1}. {colored_guess}")
            print("-" * 30)
            print(f"\n🎉 Congratulations! You've guessed the word: \033[42m\033[30m {correct_word.upper()} \033[0m 🎉")
            break
        else:
            if guess_count == max_guesses:
                # Clear screen and show final state
                clear_screen()
                print(f"\n🎯 Guess the {len(correct_word)}-letter word!")
                print("💀 GAME OVER 💀")
                print(f"Used all {max_guesses} guesses")
                
                # Show final alphabet state
                letter_tracker.display_alphabet()
                
                # Show ALL guesses
                print("\nYOUR GUESSES:")
                print("-" * 30)
                for i, colored_guess in enumerate(colored_guesses):
                    print(f"  {i+1}. {colored_guess}")
                print("-" * 30)
                
                print(f"\n💀 Game Over! The word was: \033[42m\033[30m {correct_word.upper()} \033[0m")
    
    # Ask if they want to play again
    print("\nWould you like to play again? (y/n)")
    if input().lower().startswith('y'):
        game_loop()

if __name__ == "__main__":
    game_loop()