from src.loan import Loan


class Library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.employees = []
        self.users = []
        self.loans = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def add_employee(self, employee):
        self.employees.append(employee)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book):
        if book.is_borrowed:
            print(f"{book} is already borrowed.")
            return
        if user not in self.users:
            print(f"{user} is not registered.")
            return

        book.mark_as_borrowed()
        user.borrow_book(book)
        loan = Loan(user, book)
        self.loans.append(loan)
        print(f"{user} borrowed '{book}'.")

    def return_book(self, user, book):
        book.mark_as_returned()
        user.return_book(book)

        for loan in self.loans:
            if loan.user == user and loan.book == book and loan.return_date is None:
                loan.close_loan()
                break

        print(f"{book} returned to library - {user} returned it.")

    def list_avaliable_books(self):
        available = [book for book in self.books if not book.is_borrowed]
        if not available:
            print("No available books.")
            return

        for book in available:
            print(book.get_details())

    def __str__(self):
        return f"{self.name} - {self.address}"