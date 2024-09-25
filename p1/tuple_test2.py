tuple_from_dict = (
    {
        'name': 'Dima',
        'age': 34,
    },
    {
        'name': 'Gerasim',
        'age': '66',
    }
)

print(tuple_from_dict)

tuple_from_dict[0]['age'] = 35

print(tuple_from_dict)

del tuple_from_dict[1]['age']

print(tuple_from_dict)

print('-----')

authors_books_library = ('Gogol', 'Lermontov', 'Tolstoy')

books_library = ('War and peace', 'Players', 'Humans and passions')

sum_authors_and_books = authors_books_library + books_library

print(sum_authors_and_books)

print(sum_authors_and_books.count('Tolstoy'))
print(sum_authors_and_books.index('Tolstoy'))
