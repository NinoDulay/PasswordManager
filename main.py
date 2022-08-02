from generatePassword import generateWeak,generateMedium,generateStrong
from databaseHandler import add_password, show_database, delete_password


while True:
    print("Welcome to Password Manager")
    print("What would you like to do:")
    print("1. Generate Password")
    print("2. Show Generated Passwords")
    print("3. Delete Generated Password")
    print("4. Exit")

    user_input = input(">>> ")

    if user_input == "1":
        print("For what application will you use your password?")
        application = input(">>> ")
        print()

        print("How strong should the password be:")
        print("1. Weak - 5-7 Chars, Pure Letters")
        print("2. Medium - 7-12 Chars, Letters and Numbers")
        print("3. Strong - 15-20 Chars, Letters, Numbers, and Symbols")
        pw_strength = input(">>> ")

        if pw_strength == "1":
            password = generateWeak()
        elif pw_strength == "2":
            password = generateMedium()
        elif pw_strength == "3":
            password = generateStrong()

        add_password(application, password)

        print()
        print(f"Saved Password for {application}!")

    elif user_input == "2":
        show_database()
    elif user_input == "3":
        print("Enter the application and the password you want to delete")
        app_to_delete = input("Application: ")
        pw_to_delete = input("Password: ")

        delete_password(app_to_delete, pw_to_delete)

        print()
        print(f"Password Deleted for {app_to_delete}")
    elif user_input == "4":
        print("Thank you for using this program!")
        break
