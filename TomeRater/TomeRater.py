"""
CodeAcademy Project Application to be able to read and rate books and users,
using classes.
"""


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Successfully changed email to {Updated_Email}!".format(Updated_Email = address))

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        counter = 0
        book_number = 0
        for value in self.books.values():
            if value:
                counter += value
                book_number += 1
        average = (counter / book_number if book_number > 0 else book_number)
        return average

    def __repr__(self):
        return "User: {name}, email: {email}, books read: {books_read}".format(name = self.name, email = self.email, books_read = (len(self.books)))

    def __eq__(self, another_user):
        if self.name == another_user:
            return True
        else:
            return False


class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("ISBN has been updated!")

    def add_rating(self, rating_stars):
        if (rating_stars >= 0) and (rating_stars <= 4):
            self.rating.append(rating_stars)
        else:
            print("Rating is not in between 0 - 4")

    def get_average_rating(self):
        star_rating = 0
        for value in self.rating:
            star_rating += value
        if star_rating == 0:
            average_star_rating = 0
        else:
            average_star_rating = (star_rating / len(self.rating))
        return average_star_rating

    def __eq__(self, other):
        if (self.isbn == other_isbn) and (self.title == other.title):
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{tile} by {author}".format(tile = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)


class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction_book = Fiction(title, author, isbn)
        return fiction_book

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if email not in self.users.keys():
            self.users[email].read_book(book, rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("{email} was a ghost email and does not exist!".format(email=email))

    def add_user(self, name, email, books = None):
        new_user = User(name,email)
        self.users[email] = new_user
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.keys():
            print(user)

    def get_most_read_book(self):
        most_read = None
        read_count = 0
        for book in self.books.items():
            if reads > read_count:
                read_count = reads
                most_read = book
        return most_read

    def highest_rated_book(self):
        book_current_rating = 0
        book_rated = None
        for book in self.books.keys():
            if book_current_rating < book.get_average_rating():
                book_current_rating = book.get_average_rating()
                book_rated = book.title
        return book_rated

    def most_positive_user(self):
        highest_user = None
        users_star_rating = 0
        for user in self.users.values():
            user_average = user.get_average_rating()
            if user_average > users_star_rating:
                users_star_rating = user_average
                highest_user = user
        return highest_user

