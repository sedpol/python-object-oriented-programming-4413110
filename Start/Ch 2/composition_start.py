# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects

class Author:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

        self.chapters: Chapter = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pageCount
        return result

class Chapter:
    def __init__(self, name, pageCount) -> None:
        self.name = name
        self.pageCount = pageCount

author = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, author)

b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.author)
print(b1.chapters)
print(b1.getBookPageCount())
