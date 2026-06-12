class Book:
    def __init__(self, title, author, year, genre):
        self.title= title
        self.author= author
        self.year= year
        self.genre= genre
        self.is_borrowed= False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

    def get_details(self):
        status= "Borrowed" if self.is_borrowed else "Avaliable"
        return f"{self.title} by {self.author}({self.year} - {status}"
    
    def __str__(self):
        return self.title

