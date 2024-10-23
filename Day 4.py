import random
print("Hey there in this game u have to guess a no chosen by computer from 1 to 100 ")

def guess():   
    try:
        guess = int(input("Enter you guess"))
        random_int = random.randint(1, 100)

        if guess > random_int + 20:
            result =  "Too higher value"
        elif guess >= random_int +5:
            result = "a little higher than computers's guess"
        elif guess == random_int:
            result = "Yayy!, u got it correct"
        elif guess <= random_int -5:
            result = "U r close, a little lower than actual guess"
        elif guess <= random_int -20:
            result = "Too far!, very low than actual value"

    except ValueError:
        print("Incorrect input")
def main():
    while True:
        guess()
        b = input("Do u want to continue playing (yes/no)").lower
        if b != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()