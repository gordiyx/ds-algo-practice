"""
A program for library management. For each book, store the following information: title, author, and whether the book is borrowed or not.

Functions:
    add_book(title, author_first_name, author_last_name) – adds a new book to the list,
    borrow_book(title) – sets the borrowed status of the specified book to True,
    return_book(title) – sets the borrowed status of the specified book to False,
    borrowed_books() – returns a list of books that are currently borrowed.
"""

# Library data structure: a list of book dictionaries
library = []

# Adds a new book to the library
def add_book(title, author_first_name, author_last_name):
    book = {
        "title": title,
        "author": f"{author_first_name} {author_last_name}",
        "borrowed": False
    }
    library.append(book)

# Marks the book with the given title as borrowed
def borrow_book(title):
    for book in library:
        if book["title"] == title:
            book["borrowed"] = True  # Fixed: was '==' instead of '='
            break

# Marks the book with the given title as returned
def return_book(title):
    for book in library:
        if book["title"] == title:
            book["borrowed"] = False  # Fixed: was '==' instead of '='
            break

# Returns a list of currently borrowed books
def borrowed_books():
    return [book for book in library if book["borrowed"]]


# Example usage

# Add books to the library
add_book("Algorithms in C", "Robert", "Sedgewick")
add_book("The Art of Computer Programming, Volume 1", "Donald", "Knuth")
add_book("The Art of Computer Programming, Volume 2", "Donald", "Knuth")

# Borrow two books
borrow_book("The Art of Computer Programming, Volume 1")
borrow_book("The Art of Computer Programming, Volume 2")

# Print currently borrowed books
print("List of borrowed books:")
for book in borrowed_books():
    print(f"- {book['title']}")
