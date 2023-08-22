class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_details(self):
        return (f'The book {self.title} by the author {self.author} is {self.price}$')


class Fiction(Book):
    def __init__(self, title, author, price, geners):
        super().__init__(title, author, price)
        self.geners = geners
        print(f'{super().get_details()} and it is a {self.geners} book')


class NonFiction(Book):
    def __init__(self, title, author, price, topic):
        super().__init__(title, author, price)
        self.topic = topic
        print(f'{super().get_details()} and it is a {self.topic} book')


class poetry(Book):
    def __init__(self, title, author, price, style):
        super().__init__(title, author, price)
        self.style = style
        print(f'{super().get_details()} and it is a {self.style} book')


# book1 = Book('abc','sarath',12)
# book1.get_details()
book2= Fiction('Fiction', 'sarath', 45, 'Science Fiction')
book2.get_details()
book3=NonFiction('non fiction','sai',120,"drama")
book3.get_details()
book4=poetry("farmers","balan",160,"short song")
book4.get_details()