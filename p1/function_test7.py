from datetime import date


def f_return_day_weeks():
    return date.today().strftime('%A')


def create_new_post(post, weekday=f_return_day_weeks()):
    post_copy = post.copy()
    post_copy['Created_on_weekday'] = weekday
    return post_copy


initial_post = {
    'id': 333,
    'author': 'Dmitry',
}

post_with_weekday = create_new_post(initial_post)
print(post_with_weekday)
print(initial_post)
