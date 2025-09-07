def provide_hint(guess, actual_number):
    if guess < actual_number:
        print("Your guess is too low.")
    elif guess > actual_number:
        print("Your guess is too high.")
    else:
        print("Congratualation. You guessed correctly. ")
