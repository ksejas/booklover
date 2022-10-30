import pandas as pd
import numpy as np

class BookLover:
    '''The BookLover Class '''

    def __init__(self, name, email, fav_genre):
        self.name=name
        self.email=email
        self.fav_genre=fav_genre
        self.num_books = 0
        self.book_list=pd.DataFrame({'book_name':[], 'book_rating':[]}).astype(dtype = {'book_name' : str, 'book_rating':int})

    def add_book(self, book_name, book_rating):
        '''The add_book function '''
        new_book = pd.DataFrame([{
            'book_name' : book_name,
            'book_rating' : book_rating
        }]).astype(dtype = {'book_name' : str, 'book_rating':int})
        if any(self.book_list.book_name == book_name)==True:
            print("The new book is a book that is already included in the book_list.")
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self, book_name):
        if any(self.book_list.book_name == book_name)==True:
            return True
        else:
            return False

    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list[self.book_list['book_rating']>3]
       
        
#if __name__ == '__main__':
#    test_object=BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
#    test_object.add_book("War of the Worlds", 4)
    