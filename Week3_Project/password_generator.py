import random
import string

while True:

    print("\n" + "=" * 45)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 45)

    print("1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4")
            continue

        letters = string.ascii_letters
        numbers = string.digits
        special = "@#$!%&*"

        all_characters = letters + numbers + special

        password = []

        password.append(random.choice(numbers))
        password.append(random.choice(special))

        for i in range(length - 2):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        final_password = "".join(password)

        print("\n" + "=" * 45)
        print("PASSWORD GENERATED")
        print("=" * 45)
        print("Generated Password:", final_password)
        print("=" * 45)

    elif choice == "2":
        print("Program Closed")
        break

    else:
        print("Invalid choice")