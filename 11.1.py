# Implement the following class hierarchy using Python: A publication can be either a book or a magazine. Each
# publication has a name. Each book also has an author and a page count, whereas each magazine has a chief editor.
# Also write the required initializers to both classes. Create a print_information method to both subclasses for
# printing out all information of the publication in question. In the main program, create publications Donald Duck (
# chief editor Aki Hyyppä) and Compartment No. 6 (author Rosa Liksom, 192 pages). Print out all information of both
# publications using the methods you implemented.

class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"The name of the publication is {self.name}.")

class Book(Publication):
    def __init__(self, name, author,page_count):
        self.author = author
        self.page_count = page_count
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The author of the book is {self.author} and the amount of pages is {self.page_count}.\n")

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor = chief_editor
        super().__init__(name)

    def print_information(self):
        super().print_information()
        print(f"The chief editor of the Magazine is {self.chief_editor}.\n")

publications = []
publications.append(Magazine("Donald Duck", "Aki Hyyppä"))
publications.append(Book("Compartment No. 6", "Rosa Liksom", 192))

for i in publications:
    i.print_information()