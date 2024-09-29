list_users_countries = ['Russia', 'Germany', 'China', 'USA']
list_users_counts = [15, 45, 52, 10]

lists_zip_users_counts = list(zip(list_users_countries, list_users_counts))
print(lists_zip_users_counts)

dict_users_counts = dict(lists_zip_users_counts)
print(dict_users_counts)


