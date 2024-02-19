class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title(self):
        return "Title: " + self.title

    def get_author(self):
        return "Author: " + self.author


PP = Book("Pride and Prejudice", "J.K. Rowling")
H = Book("Hamlet", "William Shakespeare")
WP = Book("War and Peace", "Lev Tolstoy")