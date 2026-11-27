def add_contact():
    name = input("Enter a Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")

    with open("contacts.txt", "a") as file:
        file.write(f"{name}|{phone}|{email}\n")

    print("Contact saved successfully!")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        if not contacts:
            print("Contact book is empty!")
            return

        print("\n======= SAVED CONTACTS =======")

        for contact in contacts:
            name, phone, email = contact.strip().split("|")

            print(f"Name: {name}")
            print(f"Phone: {phone}")
            print(f"Email: {email}")
            print("-" * 20)

    except FileNotFoundError:
        print("No contacts found!")


def search_contact():
    search_name = input("Enter a name to search: ").lower()

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        found = False

        for contact in contacts:
            name, phone, email = contact.strip().split("|")

            if search_name in name.lower():
                print("\nContact Found!")
                print(f"Name: {name}")
                print(f"Phone Number: {phone}")
                print(f"Email Address: {email}")

                found = True

        if not found:
            print("Contact not found!")

    except FileNotFoundError:
        print("No contacts found!")


def delete_contact():
    delete_name = input("Enter a name to delete: ").lower()

    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        updated_contacts = []
        found = False

        for contact in contacts:
            name, phone, email = contact.strip().split("|")

            if name.lower() == delete_name:
                found = True
            else:
                updated_contacts.append(contact)

        if found:
            with open("contacts.txt", "w") as file:
                file.writelines(updated_contacts)

            print("Contact deleted successfully!")

        else:
            print("Contact not found!")

    except FileNotFoundError:
        print("No contacts found!")


# Main program

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option from the list: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        print("Good Bye!")
        break

    else:
        print("Invalid choice! Please choose correctly!")
