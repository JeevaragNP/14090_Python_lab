class Publisher:
    def __init__(self, pubname):
        self.pubname = pubname

    def display(self):
        print("Publisher Name is:", self.pubname)


class Book(Publisher):
    def __init__(self, pubname, title, author):
        Publisher.__init__(self, pubname)
        self.author = author
        self.title = title

    def display(self):
        print("Title of the book:", self.title)
        print("Author the book:", self.author)


class Python(Book):
    def __init__(self, pubname, title, author, price, pages):
        Book.__init__(self, pubname, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        print("Title of the book:", self.title)
        print("Author the book:", self.author)
        print("Publisher Name is:", self.pubname)
        print("Price of the book is:", self.price)
        print("No of pages:", self.pages)


#b1 = Python("Alchemist", "Paulo Choelo", "DC", "500", "250")
b2 = Book("DC", "Harry Potter", "J K Rowling",)
#b1.display()
b2.display()

