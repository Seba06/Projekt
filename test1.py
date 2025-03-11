import random
# inte min kod!
def generate_feedback(secret, guess):
    feedback = []
    for i in range(len(secret)):
        if guess[i] == secret[i]:
            feedback.append("✅") 
        elif guess[i] in secret:
            feedback.append("🔠") 
        else:
            feedback.append("❌") 
    return " ".join(feedback)

def word_guess_game():
    words = ["apple", "table", "grape", "chair", "mouse"] 
    secret_word = random.choice(words)
    attempts = 5
    
    print("Welcome to the Word Guessing Game!")
    print(f"Guess the {len(secret_word)}-letter word. You have {attempts} tries!")
    
    while attempts > 0:
        guess = input("Enter your guess: ").lower()
        
        if len(guess) != len(secret_word):
            print(f"Your guess must be {len(secret_word)} letters long!")
            continue
        
        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word!")
            return
        
        feedback = generate_feedback(secret_word, guess)
        print("Feedback:", feedback)
        
        attempts -= 1
        print(f"Attempts left: {attempts}\n")
    
    print(f"Game over! The word was '{secret_word}'.")

if __name__ == "__main__":
    word_guess_game()
