class User(object):
    """ Represents a user """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):      
        return "user named {name}, with an email {email}, with {books} books read".format(name=self.name, email=self.email,books=len(self.books))

    def __eq__(self, other_user):
        try:
            return self.name == other_user.name and self.email == other_user.email
        except AttributeError:
            return False

    def __hash__(self):
        return hash((self.name, self.email))

    def get_email(self):
        return self.email

    def change_email(self, address):
        previous_email = self.email
        self.email = address
        print("{name} email has been changed from {oldemail} to {newemail}".format(name=self.name, oldemail=previous_email, newemail=address))

    def read_book(self, book, rating=None):
        if rating:            
            self.books.update({book: rating})

    def get_average_rating(self):
        book_val = 0
        num_of_books = len(self.books)    
        #TODO need to get ratings for each book
        for value in self.books.values():
            book_val += value
        return book_val / num_of_books

  

class Book(object):
    """ Represents a book. """

    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other_book):  
        try:
            return self.title == other_book.title and self.isbn == other_book.get_isbn
        except AttributeError:
            return False
     

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{title} isbn has been updated to {new_isbn}".format(title=self.title, new_isbn=self.isbn))

    def add_rating(self, rating):
        if rating !=None and (rating >= 0 and rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid rating")

    def get_average_rating(self):
        num_ratings = len(self.ratings)
        cntr = 0
        for i in range(self.ratings.count()):
            cntr += self.ratings[i]

        return cntr/num_ratings

class Fiction(Book):
    """ Represents a fiction book. """

    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def __repr__(self):
        return "{title} by {author}".format(title=Book.get_title, author=self.author)

    def get_author(self):
        return self.author

class NonFiction(Book):
    """ Represents a non - fiction book. """

    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=Book.get_title, level=self.level, subject=self.subject)

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level


class TomeRater(object):
    """ Represent main object to invoke users and book classes. """

    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)
         
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)        

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)        

    def add_book_to_user(self, book, email, rating=None):
       
        if self.users.get(email) != None:
           self.users[email].read_book(book, rating)
           book.add_rating(rating)    

           if self.books.get(book) == None:
               self.books[book] = 1
           else:
               self.add_rating(book, rating)
                           
        else:
            print("No user with email {email}!".format(email=email))

    def add_rating(self, book, rating):
        if self.books.get(book) != None:
           self.books[book] +=1
        else:
            self.books.update({book: rating})

    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None and len(user_books) >=0:
            for i in range(len(user_books)):
                self.add_book_to_user(user_books[i], email,1)
       # if type(user_books) == 'list':
       #     for book in len(user_books):
       #             self.add_book_to_user(book, email)
       #     elif type(user_books) == Book:
       #          self.add_book_to_user(user_books, email) 


    def print_catalog(self):
        for key, value in self.books.items():
            print ("Title: {title} ISBN: {isbn} Ratings: {ratings} : Read: {times_read}".format(title=key.title, isbn=key.isbn,ratings=key.ratings, times_read=value))

    def print_users(self):
        for key, value in self.users.items():
            print ("User info: Name:{name} - Email:{email} Books read:{books}".format(email=key, name=value.name,books=len(value.books)))
           
    def most_read_book(self):
        title =""
        val = 0
        for k, v in self.books.items():
            if v > val:
                title = k.title
                val = v
        print ("Most read book- Title: {0}. Book has been read {1} times".format(title,val))
