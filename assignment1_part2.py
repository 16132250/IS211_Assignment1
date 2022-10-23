
class Book:

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f'{self.title}, written by {self.author}')

if __name__ == "__main__":
    oman = Book('John Steinbeck', 'Of Mice and Men')
    tkam = Book('Harper Lee', 'To Kill a Mockingbird')

    Book.display(oman)
    Book.display(tkam)
