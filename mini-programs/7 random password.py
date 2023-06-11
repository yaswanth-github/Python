import random
import string

def generate_password(length):
    """Generate a random password of the given length."""
    # Define the character set to use for the password.
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the set.1

    password = "".join(random.choice(chars) for _ in range(length))
    return password

def main():
    """Main function to run the program."""
    # Get the desired password length from the user.
    length = int(input("Enter the desired password length: "))

    # Generate a random password of the desired length.
    password = generate_password(length)

    # Display the password to the user.
    print(f"Your random password is: {password}")

if __name__ == "__main__":
    main()
