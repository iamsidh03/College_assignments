# 📚 Library Management System – Problem Statement (Medium-Hard)
# 🎯 Objective:
# Build a system to manage books in a library using OOP principles. Each book should have a unique ID, and the system should allow borrowing, returning, adding, removing, and listing books.

# ✅ Class 1: Book
# Attributes:
# book_id (int): Unique identifier for the book

# title (str): Title of the book

# author (str): Author's name

# copies (int): Number of available copies

# Methods:
# is_available() → Returns True if copies > 0, else False

class Book:
    def __init__(self,book_id,titles,author,copies):
        self.book_id=book_id
        self.titles=titles
        self.author=author
        self.copies=copies



# ✅ Class 2: Library
# Attribute:
# books: A list to store multiple Book objects

# Methods:
# add_book(book)
# ➤ Add a book to the library only if book_id doesn't already exist
# ➤ If it exists, update the number of copies instead

# remove_book(book_id)
# ➤ Removes the book entirely if it exists

# borrow_book(book_id)
# ➤ If the book is available, decrease copies by 1
# ➤ If not available, print "Sorry, '{title}' is currently not available."

# return_book(book_id)
# ➤ Increases the number of copies by 1

# show_books()
# ➤ Display all books with:
# "ID: <id> | Title: <title> | Author: <author> | Available Copies: <copies>"

# 🧠 Bonus Tip Integration:
# Each book must be uniquely identified by its book_id.

# Avoids confusion with duplicate titles or authors.

# 💡 Example Use:
# python
# Copy
# Edit
# b1 = Book(101, "The Alchemist", "Paulo Coelho", 3)
# b2 = Book(102, "Atomic Habits", "James Clear", 5)

# lib = Library()
# lib.add_book(b1)
# lib.add_book(b2)

# lib.borrow_book(101)     # Decreases copies of The Alchemist
# lib.return_book(101)     # Increases copies of The Alchemist
# lib.show_books()