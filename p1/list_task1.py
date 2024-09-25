list_num_ratings = [1, 2.56, 'Hello', True, {'name': 'Vasily', 'age': 25}]

print(list_num_ratings)

del list_num_ratings[2]
# or def .pop()

print('Was delete 3-th e;ement of list: ',
      'List ratings', list_num_ratings, len(list_num_ratings))

list_num_ratings.reverse()

print(list_num_ratings)

list_num_elemenets = [214, 'Main']

list_num_ratings.extend(list_num_elemenets)

print(list_num_ratings)
print(list_num_elemenets)
