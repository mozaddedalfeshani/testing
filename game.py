import random


def check_guess(secret, guess):
    if guess < secret:
        return "low"
    if guess > secret:
        return "high"
    return "correct"


def play(low=1, high=100):
    secret = random.randint(low, high)
    guesses = 0
    print(f"Guess a number between {low} and {high}.")
    while True:
        guesses += 1
        guess = int(input("> "))
        result = check_guess(secret, guess)
        if result == "correct":
            print(f"You got it in {guesses} guesses!")
            return guesses
        print("Too low." if result == "low" else "Too high.")


if __name__ == "__main__":
    play()
