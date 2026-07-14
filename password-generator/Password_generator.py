import random
import string

while True:
    size = int(input("Enter password length: "))

    uppercase = input("Include uppercase? (Y/N): ").lower()
    lowercase = input("Include lowercase? (Y/N): ").lower()
    numbers = input("Include numbers? (Y/N): ").lower()
    symbols = input("Include symbols? (Y/N): ").lower()

    if size <= 0:
        print("Password length must be positive.")
        continue

    password = []
    char_pool = ""

    if uppercase == "y":
        char_pool += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))

    if lowercase == "y":
        char_pool += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))

    if numbers == "y":
        char_pool += string.digits
        password.append(random.choice(string.digits))

    if symbols == "y":
        char_pool += string.punctuation
        password.append(random.choice(string.punctuation))

    if char_pool == "":
        print("Please select at least one character type.")
        continue

    if size < len(password):
        print(f"Password length must be at least {len(password)}.")
        continue

    while len(password) < size:
        password.append(random.choice(char_pool))

    random.shuffle(password)

    password = "".join(password)

    print("\nGenerated Password:", password)

    if len(password) < 8:
        print("Strength: Weak")
    elif len(password) <= 12:
        print("Strength: Medium")
    else:
        print("Strength: Strong")

    save = input("Save password? (Y/N): ").lower()

    if save == "y":
        with open("password.txt", "a") as f:
            f.write(password + "\n")
        print("Password saved!")

    again = input("Generate another password? (Y/N): ").lower()

    if again != "y":
        print("Thank you for using My Password Generator!")
        break