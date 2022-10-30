from booklover.booklover import BookLover

BookLover1 = BookLover('Katherine', 'k@gmail.com', 'fiction')
BookLover1.add_book('Addie LaRue', 4)
howmany=BookLover1.num_books_read()
print(howmany)
