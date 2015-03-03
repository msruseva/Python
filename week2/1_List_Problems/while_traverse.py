books = ["Learn You a Haskell",
        "The Healthy Programmer",
        "Code Complete",
        "The Pragmatic Programmer",
        "Pro Git",
        "Introduction to Agorithms",
        "Concrete Mathematics"]

start_index = 0
end_index = len(books)

while start_index < end_index:
    book = books[start_index]
    print(book)
    start_index = start_index + 1
