import random

def play_guessing_game():
    # 1. Set Up the Game
    secret_number = random.randint(1, 10)
    max_attempts = 3
    attempts = 0
    
    print("--- Welcome to the Number Guessing Game ---")
    print("I have picked a number between 1 and 10. You have 3 attempts!")
    
    # Using a while loop to control the guessing rounds
    while attempts < max_attempts:
        attempts += 1
        
        try:
            guess = int(input(f"\nAttempt {attempts}: Enter your guess (1-10): "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            # continue statement: skips the rest of this iteration and starts the next attempt
            continue
            
        # Check if the guess is within the valid range
        if guess < 1 or guess > 10:
            print("Your guess is out of range! Please choose between 1 and 10.")
            continue
        else:
            # pass statement: acts as a placeholder where code could be added later (e.g., logging stats)
            pass
            
        # Check the user's guess against the secret number
        if guess == secret_number:
            print(f"Congratulations! You guessed the secret number {secret_number} correctly.")
            # break statement: immediately exits the while loop because the user won
            break
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")
            
    else:
        # else statement: executes only if the while loop finishes normally 
        # (i.e., all attempts were used without triggering a 'break')
        print(f"\nGame Over! You ran out of attempts. The secret number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    play_guessing_game()

    import random

# 1. Set Up the Game
secret_number = random.randint(1, 10)

attempts = 0
max_attempts = 3

# 2 & 3. While loop for guessing logic
while attempts < max_attempts:
    try:
        guess = int(input("Guess the number (between 1 and 10): "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    # Count valid input as an attempt
    attempts += 1

    # Check for out-of-range guess
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue  # Skip to the next iteration

    # Check the guess
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break  # Exit loop on victory
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

else:
    # Executes only if user runs out of attempts without a correct guess
    print("Better luck next time!")

    # 1. Prompt the user for input
number = int(input("Enter the number for which you want the multiplication table: "))

# 2. Generate the Multiplication Table using a for loop and range
for i in range(1, 11):
    # Calculate the product
    result = number * i
    
    # 3. Display the Multiplication Table in the requested format
    print(f"{number} x {i} = {result}")

    # 1. Define a function calculate_bmi(weight, height) that returns the BMI
def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / [height (m)]²
    return weight / (height ** 2)

# 2. Prompt the user for their weight (in kg) and height (in meters) with exact text
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# 3. Use the function to calculate and display the BMI
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")