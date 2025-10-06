class Book:
    """A class representing a book with title, author, and availability status."""
    
    def __init__(self, title, author):
        """Initialize a book with title and author. Book starts as available."""
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Check out the book, marking it as unavailable."""
        self._is_checked_out = True
    
    def return_book(self):
        """Return the book, marking it as available."""
        self._is_checked_out = False
    
    def is_available(self):
        """Return True if the book is available (not checked out)."""
        return not self._is_checked_out


class Library:
    """A class representing a library that manages a collection of books."""
    
    def __init__(self):
        """Initialize an empty library."""
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title if it's available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
    
    def return_book(self, title):
        """Return a book by title if it's checked out."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
    
    def list_available_books(self):
        """Print all available books in the library."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
