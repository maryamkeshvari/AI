class Book:
    def __init__(self,writer,pg_number):
        self.writer=writer
        self.pg_number=pg_number
    def __str__(self):
        return self.writer
    __repr__=__str__
def gp_book(books):
    gp1=[]
    gp2=[]
    for book in books:
        if book.pg_number>70:
            gp1.append(book)
            print(gp1)
        elif book.writer=="elif":
            gp2.append(book)
            print(gp2)


book1=Book("elif", 60)
book2=Book("romi", 80)
book_list=[book1,book2]
gp_book(book_list)
