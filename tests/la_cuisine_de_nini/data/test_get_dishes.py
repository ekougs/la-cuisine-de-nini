from unittest import TestCase

from la_cuisine_de_nini.data.dishes_provider import DishesProvider, get_dishes


class InMemoryDishesProvider(DishesProvider):
    def __init__(self, dishes):
        self.dishes = dishes

    def get(self):
        return self.dishes


class TestGetDishes(TestCase):
    def test_should_get_all_computed_dishes(self):
        # GIVEN
        dishes_provider = InMemoryDishesProvider(TestGetDishes._separated_dishes())

        # WHEN
        dishes = get_dishes(dishes_provider)

        # THEN
        self.assertListEqual([dish["name"] for dish in dishes],
                             ["thiep", "brochette et frites", "brochette et alloco", "poulet et frites",
                              "poulet et alloco"])

    @staticmethod
    def _separated_dishes():
        return {
            "complete_dishes": [
                {
                    "name": "thiep",
                    "lunch": True,
                    "diner": False
                },
            ],
            "main_dishes": [
                {
                    "name": "brochette",
                    "lunch": True,
                    "diner": False
                },
                {
                    "name": "poulet",
                    "lunch": True,
                    "diner": False
                },
            ],
            "side_dishes": [
                {
                    "name": "frites"
                },
                {
                    "name": "alloco"
                },
            ],
        }
