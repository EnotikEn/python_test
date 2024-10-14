# list_values = ['name', 'is', 'John', 'Cena']

# name, isi, John, Cena = list_values

# print(isi)
# print(John)

list_values = ['table', 'task', 'board']

table, *list_values_new = list_values

print(table)
print(list_values_new)
print(type(list_values_new))


print('-----')

tuple_values = ('man', 'men', 'girl')

man, *tuple_values_new = tuple_values
print(type(tuple_values))
print(man)
print(tuple_values_new)
print(type(tuple_values_new))
