# Library to lend and donate books
class Library:
    pass
    def __init__(self,lstOfBooks,libname):
        self.lstOfBooks=lstOfBooks
        self.libname= libname
        self.lendict = {}
    # display all Libaray books
    def displayBook(self):
        print(f"List of books in Library {self.libname}")
        for books in self.lstOfBooks:
            print(books)
    # lend books
    def lendBook(self,user,book):
        if book not in self.lstOfBooks:
            print("Sorry Book is not available")
        else:
            if book not in self.lendict.keys():
                self.lendict.update({book:user})
                print("Requested Book has been updated, You can take "
                      "Book")
            else:
                print(f"Sorry,Book is already taken by {self.lendict[book]}")
    # add books to library
    def donateBook(self,book):
        self.lstOfBooks.append(book)
        print("Book has been added to the book list")
    # return book
    def returnBook(self,book):
        self.lendict.pop(book)
if __name__ == '__main__':
    bookLists = Library(['PYTHON','JAVA', 'SQL', 'HTML', 'CSS', 'PHP', 'RUBY'], "Coding")
    while(True):
        print(f"Welcome to the {bookLists.libname} library. Enter your choice to continue")
        print("1. Display Books\n2. Lend Books\n3. Donate Books\n4. Return Books")
        userChoice = input()
        if userChoice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            userChoice = int(userChoice)
        if userChoice == 1:
            bookLists.displayBook()
        elif userChoice == 2:
            book = input("Enter the name of the book you want to lend:").upper()
            user = input("Enter your name")
            bookLists.lendBook(user, book)
        elif userChoice == 3:
            book = input("Enter the name of the book you want to donate:")
            bookLists.donateBook(book)
        elif userChoice == 4:
            book = input("Enter the name of the book you want to return:")
            bookLists.returnBook(book)
        else:
            print("Not a valid option")
        print("Press q to quit and c to continue")
        quitContinue = ""
        while(quitContinue!="c" and quitContinue!="q"):
            quitContinue = input().lower()
            if quitContinue == "q":
                exit()
            elif quitContinue == "c":
                continue
            else:
                print("Not a valid option. Enter 'q' for Quit and 'c' for Continue")
                continue
