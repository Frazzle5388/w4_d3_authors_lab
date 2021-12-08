from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author('John')
author2 = Author('Bob')

book1 = Book('Nae bother', author1)
book2 = Book('Aye but, Nae but', author2)

author_repository.save(author1)
author_repository.save(author2)
book_repository.save(book1)
book_repository.save(book2)


for author in author_repository.select_all():
    print(author.__dict__)
    
for book in book_repository.select_all():
    print(book.__dict__)