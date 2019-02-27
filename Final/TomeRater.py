class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "The email has been updated to " + address

    def __repr__(self):
        return "User: " + self.name + "\nemail: " + self.email + "\nbooks read: " + str(len(self.books.values()))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        sum = 0
        average = 0
        for book in self.books.keys():
            if self.books[book] != None:
                sum += self.books[book]
                average += 1
        return sum / average


class Book():
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.rating = []

    def __repr__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "The ISBN number has been updated to " + str(new_isbn)

    def set_price(self, new_price):
        self.price = new_price
        return "The new price is " + str(new_price)

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            print("Invalid rating")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        if len(self.rating) == 0:
            return None
        sum = 0
        for rating in self.rating:
            sum += rating
        return sum / len(self.rating)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "Users: {}\nBooks: {}".format(self.users, self.books)

    def create_book(self, title, isbn, price):
        book = Book(title, isbn, price)
        return book

    def create_novel(self, title, author, isbn, price):
        novel = Fiction(title, author, isbn, price)
        return novel

    def create_non_fiction(self, title, subject, level, isbn, price):
        non_fiction = Non_Fiction(title, subject, level, isbn, price)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)

            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1

        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books=None):
        if email in self.users:
            print('The user already exists!')
        else:
            user = User(name, email)
            self.users[email] = user
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)

    def print_catalog(self):
        print('Book catalog:')
        for book in self.books.keys():
            print(book)

    def print_users(self):
        print('Users:')
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read_book = ''
        read_count = 0
        for book in self.books:
            if self.books[book] > read_count:
                read_count = self.books[book]

            if self.books[book] == read_count:
                most_read_book = book

            return most_read_book

    def highest_rated_book(self):
        best_book = None
        highest_rating = 0
        for book in self.books.keys():
            rating = book.get_average_rating()
            if book.get_average_rating() > highest_rating:
                best_book = book
                highest_rating = rating
        return best_book

    def most_positive_user(self):
        highest_rating = 0
        highest_rated_user = ''
        for user in self.users.values():
            average = User.get_average_rating(self)
            if User.get_average_rating(self) > highest_rating:
                highest_rating = User.get_average_rating(self)
                highest_rated_user = user
        return highest_rated_user

    def get_n_most_expensive_books(self, n):
        most_expensive_books = []
        for book in self.books.keys():
            most_expensive_books.append((book.price))
        most_expensive_books.sort()

        for n in most_expensive_books:
            if n > len(most_expensive_books):
                n = len(most_expensive_books)

        return most_expensive_books[::-1]

    def get_worth_of_user(self, user_email):
        user = self.users[user_email]
        total_worth = 0
        
        for book in user.books:
            total_worth += book.price
        return "The total price of the books owned by {} is ${}.".format(user.name, total_worth)
