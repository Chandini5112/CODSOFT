import random
import string

def generate_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password


def main():
    while True:
        try:
        # Prompt the user to specify the desired length of the password
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Length must be greater than zero.")
                continue

            # Generate the password
            password = generate_password(length)

            # Display the generated password
            print("Generated Password:", password)

        except ValueError:
            print("Please enter a valid integer for the password length.")

if __name__ == "__main__":
    main()