class Library:
    def __init__(self):
        self.books = []
        self.lended_books = {}

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print("-", book)

    def add_book(self, book):
        self.books.append(book)
        print(book, "has been added to the library.")

    def lend_book(self, book, user):
        if book in self.books and book not in self.lended_books:
            self.lended_books[book] = user
            print(book, "has been lended to", user)
        elif book in self.lended_books:
            print(book, "is already lended to", self.lended_books[book])
        else:
            print(book, "is not available in the library.")

    def return_book(self, book):
        if book in self.lended_books:
            self.lended_books.pop(book)
            print(book, "has been returned.")
        else:
            print(book, "was not lended.")


library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()
    elif choice == "2":
        book = input("Enter book name to add: ")
        library.add_book(book)
    elif choice == "3":
        book = input("Enter book name to lend: ")
        user = input("Enter user name: ")
        library.lend_book(book, user)
    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)
    elif choice == "5":
        print("Exiting Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
