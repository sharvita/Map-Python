import Book


class PrintedBook(Book.Book):
    number_of_pages = None
    date_printed = None

    def get_number_of_pages(self):
        return self.number_of_pages

    def set_number_of_pages(self, number_of_pages):
        self.number_of_pages = number_of_pages

    def get_date_printed(self):
        return self.date_printed

    def set_date_printed(self, date_printed):
        self.date_printed = date_printed

    def to_string(self):
        return "\nType: Printed Book" + super().to_string() + \
            "\nNumber of pages: " + self.get_number_of_pages() + \
            "\nDate printed: " + self.get_date_printed()
