# Simple Library Management System

library = {}   # dictionary to store books and quantity

def librarian_login():
    username = input("Enter librarian username: ")
    password = input("Enter librarian password: ")

    if username == "admin" and password == "lib123":
        print("Login successful!\n")
        return True
    else:
        print("Invalid login. Access denied.")
        return False

def add_book():
    name = input("Enter book name: ")
    qty = int(input("Enter quantity: "))
    if name in library:
        library[name] += qty
    else:
        library[name] = qty
    print("Book added successfully!\n")

def view_books():
    if not library:
        print("Library is empty.\n")
    else:
        print("Available books:")
        for book, qty in library.items():
            print(book, ":", qty)
        print()

def issue_book():
    name = input("Enter book name to issue: ")
    if name in library and library[name] > 0:
        library[name] -= 1
        print("Book issued successfully!\n")
    else:
        print("Book not available.\n")

def return_book():
    name = input("Enter book name to return: ")
    if name in library:
        library[name] += 1
    else:
        library[name] = 1
    print("Book returned successfully!\n")

if librarian_login():
    while True:
        print("----- Library Menu -----")
        print("1. Add Book")
        print("2. View Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("Thank you! Exiting Library System.")
            break
        else:
            print("Invalid choice. Try again.\n")