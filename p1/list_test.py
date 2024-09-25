
users = [
    {
        'user_id': 0,
        'user_name': 'D_Oleynikov'
    },
    {
        'user_id': 1,
        'user_name': 'D_Oleynikov8'
    },
    {
        'user_id': 2,
        'user_name': 'Admin'
    }
]

new_list_for_users = {
    'user_id': int(input('Enter your id: ')),
    'user_name': input('Enter your name: ')
}

users.append(new_list_for_users)

print('Add 2 list to 1 list: ', users)

print('(Comment) I add last list of list ''Users'':''', new_list_for_users)

removed_list_for_users = users.pop()

print(users)

print('(Comment) I remove last list of list ''Users'':''', removed_list_for_users)

ratings = [float(input('1 value: ')), float(input('2 value: ')),
           float(input('3 value: ')), float(input('4 value: '))]

print('Current rating', ratings)

print('Min value ratings', min(ratings))
print('Max values rating', max(ratings))

print('Average value rating', max(ratings)/len(ratings))

ratings_other = [4.6, 5.0, 2.3, 3.1, 2.7, 3.3]

all_sum_retings = ratings + ratings_other

print(all_sum_retings)

cut_list = all_sum_retings[3:7]

print('Output list from 3 element to 6', cut_list)

ratings_copy_list_new_object = ratings.copy()

print(ratings_copy_list_new_object)

print('id lists: ', id(ratings_copy_list_new_object), id(
    ratings), id(ratings_copy_list_new_object) == id(ratings))

rating_copy_list_link = ratings

print('id lists: ', rating_copy_list_link == ratings,
      id(rating_copy_list_link), id(ratings))
