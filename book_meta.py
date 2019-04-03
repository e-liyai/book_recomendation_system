
def book_meta(isbn, books):
    title = books.at[isbn, 'title']
    author = books.at[isbn, 'author']
    return title, author