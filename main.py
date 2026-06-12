from src.author import Author
from src.book import Book
from src.employee import Employee
from src.library import Library
from src.user import User

library = Library("Darmstadt Center Library", "FrankfurterLand Str.")

author1 = Author("Oguz Atay", "Turkish", 1960)
author2 = Author("Yasar Kemal", "Turkish", 1955)

book1 = Book("Tutunamayanlar", author1, 1980, "Edebiyat")
book2 = Book("Ince Mehmet", author2, 1960, "Edebiyat")

user1= User("Piotr", "L001")
user2= User("Selim", "L002")

employee1= Employee("Eva", "E001", any )

employee1.add_book(library, book1)
employee1.add_book(library, book2)

employee1.register_user(library, user1)
employee1.register_user(library, user2)

print("\n --Avaliable Books--")
library.list_avaliable_books()

print("\n --Borrowing--")
library.borrow_book(user2,book1)
library.borrow_book(user1,book2)

print("\n--Avaliable Books After Borrow--")
library.list_avaliable_books

print("\n --Returning--")
library.return_book(user2,book1)

print("\n--- Available Books After Return ---")
library.list_avaliable_books()