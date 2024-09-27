set_inventory_hero_1 = {'aff', 'uff', 'off', 'f', 'i', 'c'}
set_inventory_hero_2 = {'af', 'uf', 'o', 'g', 's', 'c'}

print(set_inventory_hero_1.intersection('affc'))
print(set_inventory_hero_1.intersection('a', 'f', 'f', 'c'))

sum_inventory_heroes = set_inventory_hero_1.union(set_inventory_hero_2)
print(sum_inventory_heroes)

print(set_inventory_hero_1 == set_inventory_hero_2)

print(set_inventory_hero_2.difference(set_inventory_hero_1))
print(set_inventory_hero_1.difference(set_inventory_hero_2))
# or
print(set_inventory_hero_1 - set_inventory_hero_2)
