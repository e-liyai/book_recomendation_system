import pandas as pd
from book_meta import book_meta
dataFile = 'data/BX-Book-Ratings.csv'
bookFile = 'data/BX-Books.csv'

data = pd.read_csv(dataFile, sep=';', header=0, names=['user', 'isbn', 'rating'])
books = pd.read_csv(bookFile, sep=';', header=0, error_bad_lines=False, usecols=[0,1,2], index_col=0, names=['isbn', 'title', 'author'])

print(data.head())
print(books.head())

print(book_meta('0002005018', books))

def fav_books(user, N):
    newdata = data[data['isbn'].isin(books.index)]
    userRatings = newdata[data['user'] == user]
    sortedRatings = pd.DataFrame.sort_values(userRatings, ['rating'], ascending=[0])[:N]
    sortedRatings['title'] = sortedRatings['isbn'].apply(book_meta, args=(books,))
    return sortedRatings

print(fav_books(204622, 5))