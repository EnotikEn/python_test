def update_car_info(**car):
    car['is_available'] = True
    return car


print(update_car_info())
result = update_car_info(brand='BMW', price=100000)
print(result)
