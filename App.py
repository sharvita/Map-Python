import PrintedBook
import ElectronicBook
import Author

bookList = []


def add_book():
    type = input("1) Printed Book\n"
                 "2) Electronic Book\n")

    if type[0] == '1':
        printedBook = PrintedBook.PrintedBook()
        printedBook.set_title(input("Enter the book title: "))
        printedBook.set_year_pub(input("Enter the year published: "))
        printedBook.set_location_code(input("Enter location code: "))
        while True:
            printedBook.add_author(input("Enter author name: "))
            again = input("Enter another author.Yes or no:  ")
            if len(again) == 0:
                None
            elif again[0] == 'no' :
                break
        printedBook.set_number_of_pages(input("Enter the number of pages: "))
        printedBook.set_date_printed(input("Enter the date of print: "))
        printedBook.set_publisher(input("Enter the name of the publisher: "))
        bookList.append(printedBook)
        del printedBook
    elif type[0] == '2':
        electronic = ElectronicBook.ElectronicBook()
        electronic.set_title(input("Enter the book title: "))
        electronic.set_year_pub(input("Enter the year published: "))
        electronic.set_location_code(input("Enter location code: "))
        while True:
            electronic.add_author(input("Enter author name: "))
            again = input("Enter another author yes or no: ")
            if len(again) == 0:
                None
            elif again[0] == 'no' or again[0] == 'No':
                break
                electronic.set_number_of_pages(input("Enter the number of pages: "))
                electronic.set_date_digitized(input("Enter the date of print: "))
                electronic.set_publisher(input("Enter the name of the publisher: "))
        bookList.append(electronic)
        del electronic
    else:
        print("Invalid option. Try again")


def add_author():
    title = input("Enter the title of the book you want to add an author to: ")

    for book in bookList:
        if book.get_title() == title:
            while True:
                book.add_author(input("Enter author name: "))
                again = input("Enter another author y/n")
                if len(again) == 0:
                    None
                elif again[0] == 'n' or again[0] == 'N':
                    return
    print("No such book")



def remove_author():
    title = input("Enter the title of the book whose authors you want to edit: ")

    for book in bookList:
        if book.get_title() == title:
            name = input("Enter the name of the author you want to delete: ")
            for auth in book.authors:
                if book.authors[auth] == name:
                    del book.authors[auth]
                    return
    print("No such book")


def print_title():
    for book in bookList:
        print(book.get_title())



while True:
    option = input("Menu:\n"
                   "1) Add Book\n"
                   "2) Add Author to Book\n"
                   "3) Remove Author\n"
                   "4) Print Book titles\n"
                   "5) Exit\n")

    if len(option) == 0:
        None
    elif option[0] == '1':
        add_book()
    elif option[0] == '2':
       add_author()
    elif option[0] == '3':
        remove_author()
    elif option[0] == '4':
        print_title()
    elif option[0] == '5' :
        exit(0)

    else:
        print("Enter a valid option.")
