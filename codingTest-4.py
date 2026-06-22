class Book:
    def __init__(self,title,):
        self.title = title
        self.is__borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(self.title, "borrowed")

    def return_book(self):
        self.is_borrowed = False
        print(self.title, "returned")

b1 = Book("Book1")
b2 = Book("Book2")
b3 = Book("Book3")

b1.borrow()
b1.return_book()
