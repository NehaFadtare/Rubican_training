books = [
    "Python Programming",
    "Java Programming",
    "Data Structures",
    "Machine Learning",
    "Web Development"
]

class Available_books:
    def __iter__(books):
        for i in books:
            print(i)

a1 = Available_books()
a1.__iter__(books)
