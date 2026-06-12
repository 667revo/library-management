class Employee:
    def __init__(self,name, employee_id, position):
        self.name= name
        self.employee_id= employee_id
        self.position= position


    def add_book(self, library, book):
        library.add_book(book)
        return f"{book} added to {library}"

    def remove_book(self, book, library):
        library.remove_book(book)
        print(f"{book} removed from {library}")

    def borrow_book(self, book, userid, library):
        library.borrow_book(book)
        print(f"{book} borrowed to {userid} from {library}")

    def register_user(self, library, user):
        library.register_user(user)
        print(f"{user} registered to {library}")

    
    def __str__(self):
        return f"{self.name} - {self.position}"