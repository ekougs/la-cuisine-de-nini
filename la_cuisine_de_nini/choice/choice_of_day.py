import random

from la_cuisine_de_nini.data.dishes_provider import get_dishes


def get_dishes_of_day(get_dishes_fn=get_dishes):
    dishes = get_dishes_fn()
    nb_dishes = len(dishes)
    return [dishes[random.randint(0, nb_dishes)], dishes[random.randint(0, nb_dishes)], ]
