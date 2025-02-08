import json

PASSWORD_FILE = "passwords.json"

def load_passwords():
    """Load passwords from the JSON file or create a new file if it doesn't exist."""
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_passwords(passwords):
    """Save passwords to the JSON file."""
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file, indent=4)

def add_password():
    """Add a new password entry."""
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    passwords = load_passwords()
    passwords[website] = {"username": username, "password": password}
    save_passwords(passwords)

    print("Password saved successfully!")

def retrieve_password():
    """Retrieve a stored password."""
    website = input("Enter website to retrieve password: ")
    passwords = load_passwords()

    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("No password found for this website!")

def main():
    """Main function to interact with the user."""
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
