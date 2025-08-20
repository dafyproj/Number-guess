import random

def play_guessing_game():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("Привет! Я загадал число от 1 до 20.")
    print("Попробуй угадать!")

    while True:
        try:
            guess = int(input("Введи число: "))
            attempts += 1

            if guess < number_to_guess:
                print("Слишком мало!")
            elif guess > number_to_guess:
                print("Слишком много!")
            else:
                print(f"Угадал! Это было {number_to_guess}. Попыток: {attempts}")
                break
        except ValueError:
            print("Пожалуйста, введи целое число.")

play_guessing_game()