import itertools
import json

import requests

from la_cuisine_de_nini.data.dishes_domain import DishesSchema


class DishesProvider:
    def get(self):
        raise NotImplementedError


class DishesJsonEditorOnlineProvider(DishesProvider):
    def __init__(self, menu_json_id="9459a6c670078e035243a242a642963c"):
        self.menu_json_id = menu_json_id

    def get(self):
        cuisine_de_nini_response = requests.get(f"http://api.jsoneditoronline.org/v1/docs/{self.menu_json_id}")
        cuisine_de_nini_content_dict = \
            json.loads(s=cuisine_de_nini_response.content, encoding=cuisine_de_nini_response.encoding)
        cuisine_de_nini_dict = json.loads(cuisine_de_nini_content_dict["data"])
        return cuisine_de_nini_dict


def _compute_dishes(main_dishes, side_dishes):
    return [
        {
            "name": "{} et {}".format(raw_computed_dish[0]["name"], raw_computed_dish[1]["name"]),
            "lunch": raw_computed_dish[0]["lunch"],
            "diner": raw_computed_dish[0]["diner"],
        }
        for raw_computed_dish in itertools.product(main_dishes, side_dishes)]


def get_dishes(dishes_provider=DishesJsonEditorOnlineProvider()):
    separated_dishes = dishes_provider.get()
    errors = DishesSchema().validate(separated_dishes)
    if bool(errors):
        raise ValueError(f"Dishes retrieved from server are invalid {errors}")
    dishes = separated_dishes["complete_dishes"]
    dishes.extend(_compute_dishes(separated_dishes["main_dishes"], separated_dishes["side_dishes"]))
    return dishes
