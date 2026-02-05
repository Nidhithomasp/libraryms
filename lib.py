# Simple Library Management System with Librarian Login

library = {}   # Dictionary to store books and quantities

# ---------------- Librarian Login ----------------
def librarian_login():
    username = input("Enter librarian username: ")
    password = input("Enter librarian password: ")

    if username == "admin" and password == "lib123":
        print("\nLogin successful!\n")
        return True
    else:
        print("\nInvalid login. Access denied.")
        return False


# ---------------- Library Functions ----------------
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
            print(f"{book} : {qty}")
        print()


def search_book():
    name = input("Enter book name to search: ")
    if name in library:
        print(f"Book found! Available copies: {library[name]}\n")
    else:
        print("Book not found in library.\n")


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


# ---------------- Main Program ----------------
if librarian_login():
    while True:
        print("----- Library Menu -----")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            issue_book()
        elif choice == 5:
            return_book()
        elif choice == 6:
            print("Thank you! Exiting Library System.")
            break
        else:
            print("Invalid choice. Try again.\n")
