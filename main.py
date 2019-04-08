import pandas as pd
from book_meta import book_meta
from fav_books import fav_books

dataFile = 'data/BX-Book-Ratings.csv'
bookFile = 'data/BX-Books.csv'

data = pd.read_csv(dataFile, sep=';', header=0, names=['user', 'isbn', 'rating'])
books = pd.read_csv(bookFile, sep=';', header=0, error_bad_lines=False, usecols=[0,1,2], index_col=0, names=['isbn', 'title', 'author'])

# print(data.head())
# print(books.head())
#
# print(book_meta('0002005018', books))
# print(fav_books(204622, 5, data, books))

print(data.shape) # number of rows and columns

user_per_isbn = data.isbn.value_counts()

data = data[data['isbn'].isin(user_per_isbn[user_per_isbn > 10].index)]