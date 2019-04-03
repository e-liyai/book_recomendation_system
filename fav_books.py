import pandas as pd
from book_meta import book_meta

def fav_books(user, N, data, books):
    newdata = data[data['isbn'].isin(books.index)]
    userRatings = newdata[data['user'] == user]
    sortedRatings = pd.DataFrame.sort_values(userRatings, ['rating'], ascending=[0])[:N]
    sortedRatings['title'] = sortedRatings['isbn'].apply(book_meta, args=(books,))
    return sortedRatings