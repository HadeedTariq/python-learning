class LibrarySystem:
    borrow_count = 0

    def __init__(self, title, publication_date):
        self.title = title
        self.publication_date = publication_date

    def borrow_item(self):
        self.borrow_count += 1

    def display_details(self):
        print(f"Title: {self.title}, Publication Date: {self.publication_date}")


class Book(LibrarySystem):
    borrow_count = 0

    def __init__(self, title, publication_date, author):
        super().__init__(title, publication_date)
        self.author = author

    def borrow_item(self):
        super().borrow_item()
        self.borrow_item += 1

    def display_details(self):
        super().display_details()
        print(f"Author: {self.author}")


class Magzine(LibrarySystem):
    borrow_count = 0

    def __init__(self, title, publication_date, volume):
        super().__init__(title, publication_date)
        self.volume = volume

    def borrow_item(self):
        super().borrow_item()
        self.borrow_item += 1

    def display_details(self):
        super().display_details()
        print(f"Volume: {self.volume}")


book1 = Book("Pragmatic Programmer", "2024", "John doe")
book2 = Book("Pragmatic Programmer 2", "2030", "John doe")

book1.borrow_item()
book2.borrow_item()
