class User:
    def __init__(self, name, user_id):
        self.name= name
        self.user_id= user_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        self.borrowed_books.remove(book)

    def list_borrowed_books(self):
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books."
        return [str(book) for book in self.borrowed_books]
    

    def __str__(self):
        return f"{self.name}, (ID: {self.user_id})"
        

