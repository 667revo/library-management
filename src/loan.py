from datetime import date


class Loan:

    def __init__(self, user, book):
        self.user= user
        self.book= book
        self.borrow_date= date.today()
        self.return_date= None

    def close_loan(self):
        self.return_date = date.today()

    def __str__(self):
        return f"{self.user} borrowed {self.book} on {self.borrow_date}"
