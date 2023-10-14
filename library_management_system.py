# This program is handle the library management such as book shelfing,
# issuing and borrowing books, etc.

# creating a class named Library to make a template of blockes

class Library:
    def __init__(self, books):
        self.books = books
    def show_avail_books(self):
        print("The following books are available to borrow:")
        print("-----------------------------------------------")
        for book, borrower in self.books.items():
            if borrower == 'Free':
                print(book)

    def lend_book(self, requested_book, name):
         if self.books[requested_book] == 'Free':
              print(
                   f'{requested_book} has been marked'
                   f' as \'Borrowed\' by: {name}')
              self.books[requested_book] = name
              return True
         else:
              print(
                   f'Sorry, the {requested_book} is currently'
                   f' on loan to: {self.books[requested_book]}'
              )
              return False
    
    def return_book(self, returned_book):
         self.books[returned_book] = 'Free'
         print(f'Thank you for returning {returned_book}')
