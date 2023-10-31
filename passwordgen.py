import random
import string

def generate_password(length):
    if length < 12:
        return "Password length should be at least 12 characters."

    # Define character sets for each category
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(symbols)

    # Generate the rest of the password
    remaining_length = length - 4
    all_characters = lowercase_letters + uppercase_letters + digits
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters in the password
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length < 12:
            print("Password length should be at least 12 characters.")
            return

        num_passwords = 50

        with open("passwords.txt", "w") as file:
            for _ in range(num_passwords):
                password = generate_password(length)
                reverse_password = password[::-1]  # Create the reverse of the password
                combined_passwords = f"{password} {reverse_password}"  # Combine both passwords with a space
                file.write(combined_passwords + "\n")

        print(f"{num_passwords} pairs of passwords generated and saved to 'passwords.txt'")
    except ValueError:
        print("Invalid input. Please enter a valid password length.")

if __name__ == "__main__":
    main()