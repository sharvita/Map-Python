
import Author
import Publisher

class Book:
    title = None
    year_pub = None
    location_code = None
    publisher = Publisher.Publisher()
    authors = {}

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_year_pub(self):
        return self.year_pub

    def set_year_pub(self, year_pub):
        self.year_pub = year_pub

    def get_location_code(self):
        return self.location_code

    def set_location_code(self, location_code):
        self.location_code = location_code

    def set_publisher(self, publisher):
        self.publisher.set_publisher(publisher)

    def add_author(self, name):
        author = Author.Author(name)
        self.authors.update({author: author.get_name()})

    def print_authors(self):
        for author in self.authors:
            print(self.authors[author])

    def to_string(self):
        return "\nTitle: " + self.get_title() + \
               "\nYear Published: " + str(self.get_year_pub()) + \
               "\nLocation Code: " + self.get_location_code() + \
               "\nPublisher: " + self.publisher.get_publisher()
