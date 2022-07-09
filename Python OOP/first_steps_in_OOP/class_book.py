class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'"{self.name}" by {self.author} has {self.pages} pages'


b = Book('Other Boleyn girl', 'Philipa Gregory', 500)


print(b)
print(b.name)
print(b.author)