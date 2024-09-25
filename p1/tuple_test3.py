engine_bmw = input('Enter name model engine BMW: ')
engine_mercedes = input('Enter name model engine Mercedes: ')
engine_audi = input('Enter name model engine Audi: ')

auto_engines = (engine_bmw, engine_mercedes, engine_audi)
print(auto_engines)

list_engines = list(auto_engines)
print(list_engines)

list_engines.append('No name')
print(list_engines)

auto_engines = tuple(list_engines)
print(auto_engines)
