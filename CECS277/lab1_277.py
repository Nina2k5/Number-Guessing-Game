import random
import check_input

def main():
    target = random.randint(1, 100)
    guess_count = 0
    guess = 0

    print("-Guessing Game-")
    print("I'm thinking of a number between 1 and 100. Guess the correct number!")

    #loops until guess matches random integer
    while guess != target:
        guess = check_input.get_int_range("Enter your guess (1-100): ", 1, 100)
        
        #valid guess then increment
        guess_count += 1

        #comparisons to target number
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")

    #guess == target
    print(f"Congratulations! You've guessed the number {target} in {guess_count} attempts.")

if __name__ == "__main__":
    main()