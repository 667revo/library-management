class Author:
    def __init__(self, name, nationality, birth_year):
        self.name = name
        self.nationality = nationality
        self.birth_year = birth_year

    def get_details(self):
        return f"{self.name} ({self.nationality}, {self.birth_year})"

    def __str__(self):
        return self.name
