import random
print("Hey there! In this game, you have to guess a number chosen by the computer from 1 to 100.")

def guess(random_int):   
    try:
        user_guess = int(input("Enter your guess: "))

        if user_guess > random_int + 20:
            return "Too high! You're far from the correct value."
        elif user_guess > random_int + 5:
            return "You're a little higher than the computer's guess."
        elif user_guess == random_int:
            return "Yayy! You got it correct!"
        elif user_guess < random_int - 20:
            return "Too low! You're far from the correct value."
        elif user_guess < random_int - 5:
            return "You're a little lower than the computer's guess."
        else:
            return "You're very close!"
    
    except ValueError:
        return "Incorrect input! Please enter a valid number."


def main():
    random_int = random.randint(1, 100)  # Generate a random number once

    while True:
        result = guess(random_int)
        print(result)

        # If the guess is correct, exit the loop
        if result == "Yayy! You got it correct!":
            break

        b = input("Do you want to continue playing (yes/no)? ").lower()
        if b != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
