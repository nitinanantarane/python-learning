secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    converted = int(input("Guess "))
    guess_count += 1
    if (converted == secret_number) :
        print("You Won!")
        break
else:
    print("Sorry, you failed!")