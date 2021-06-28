class Library:
    def __init__(self, list, name):
        self.booklist = list  # initializing book list
        self.name = name  # setting librabry name
        self.lendDict = {}  # initializing lending dictionary - keep track of lended book and person

    def displayBook(self):
        for book in self.booklist:  # traversing booklist
            print(book)

    def addBook(self, book):
        self.booklist.append(book)  # adding a new book in booklist
        print(f"The book {book} has been added succesfully!!")

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():  # checking if book is already lended or not
            self.lendDict.update({book: user})
            print("The book has been lended.You can take your book now!!")
        else:
            print(f"Sorry. The book has been lended to {self.lendDict[book]}")

    def returnBook(self, book):
        self.lendDict.pop(book)  # removing book from lendDict
        print(f"The book {book} has been returnd have a nice day!!")


if __name__ == '__main__':
    Lib = Library(['Rich dad Poor dad', 'How to win friends and influense people',
                  'The monk who sold is ferrari', 'Think and become rich', 'Think like a monk'], "ReadersLibrary")

    while True:
        print(f"Welcome to {Lib.name}. Enter your choices...")
        print("1. Display books")
        print("2. Lend a books")
        print("3. Add a books")
        print("4. Return a books")

        user_choice = input()

        if user_choice == '1':
            Lib.displayBook()
        elif user_choice == '2':
            book = input("Which book you want to lend: ")
            user = input("Enter your user name: ")
            Lib.lendBook(user, book)
        elif user_choice == '3':
            book = input("Enter the name of the book: ")
            Lib.addBook(book)
        elif user_choice == '4':
            book = input("Enter the name of the book: ")
            Lib.returnBook(book)
        else:
            print("Invalid choice...")

        print("Enter q to continue and c to exit")
        choice = ''
        while choice != 'q' and choice != 'c':
            choice = input()
            if choice == 'q':
                exit()
            elif choice == 'c':
                continue
