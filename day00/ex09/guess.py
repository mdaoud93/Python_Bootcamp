import sys
import random



secret_number = random.randint(1, 99)
print(secret_number)
print("\033[32mThis is an interactive guessing game!\033[0m")
print("\033[32mYou have to enter a number between 1 and 99 to find out the secret number.\033[0m")
print("\033[32mType \033[93m'exit'\033[32m to end the game.\033[0m")
print("\033[32mGood luck!\033[0m")

guess = 0
counter = 1
while (guess != secret_number):
    user_input = input()
    if (user_input == "exit"):
        print("\033[93mGoodbye\033[0m")
        sys.exit(0)
    try:
        guess = int(user_input)
    except ValueError:
        print("\033[93mPlease enter a number between 1 and 99, type 'exit' to end the game\033[0m")
        continue
    if (guess not in range(1, 100)):
        print("\033[93mPlease enter a number between 1 and 99, type 'exit' to end the game\033[0m")
        continue
    if (guess > secret_number):
        print("Too high!")
        print("What's your guess between 1 and 99?")
        counter = counter + 1
    elif (guess < secret_number):
        print("Too low!")
        print("What's your guess between 1 and 99?")
        counter = counter + 1
    else:
        if (secret_number == 42):
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if (counter == 1):
            print("Congratulations! You got it on your first try!")
        else:
            print("You won in " + str(counter) + " attempts")
