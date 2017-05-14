import random

from la_cuisine_de_nini.data.dishes_provider import get_dishes


class Rule(object):
    def get_indices_to_recompute(self, dishes):
        raise NotImplementedError


class AndRule(Rule):
    def __init__(self, *rules):
        self.rules = rules

    def get_indices_to_recompute(self, dishes):
        indices_to_recompute = []
        for rule in self.rules:
            rule_indices_to_recompute = rule.get_indices_to_recompute(dishes)
            if rule_indices_to_recompute is not None:
                indices_to_recompute.extend(rule_indices_to_recompute)
        return list(sorted(set(indices_to_recompute)))


class LunchRule(Rule):
    def get_indices_to_recompute(self, dishes):
        if not dishes[0]["lunch"]:
            return [0]


class DinerRule(Rule):
    def get_indices_to_recompute(self, dishes):
        if not dishes[1]["diner"]:
            return [1]


_rules = [
    LunchRule(),
    DinerRule(),
]


def _get_random_dish(dishes):
    return dishes[random.randint(0, len(dishes))]


def _check_rule(rule, indices_to_compute, chosen_dishes):
    indices_to_recompute = rule.get_indices_to_recompute(chosen_dishes)
    if indices_to_recompute is not None:
        indices_to_compute.extend(indices_to_recompute)
        indices_to_compute = list(sorted(set(indices_to_compute)))
    return indices_to_compute


def _compute_potential_dishes(dishes, composed_rule, indices_to_compute, chosen_dishes):
    for index_to_compute in indices_to_compute:
        chosen_dish = _get_random_dish(dishes)
        if index_to_compute < len(chosen_dishes):
            chosen_dishes[index_to_compute] = chosen_dish
        else:
            chosen_dishes.append(chosen_dish)
    return chosen_dishes, composed_rule.get_indices_to_recompute(chosen_dishes)


def get_dishes_of_day(get_dishes_fn=get_dishes, rules=_rules):
    dishes = get_dishes_fn()
    chosen_dishes = []
    indices_to_compute = [0, 1]
    composed_rule = AndRule(*rules)
    while len(indices_to_compute) > 0:
        chosen_dishes, indices_to_compute = \
            _compute_potential_dishes(dishes, composed_rule, indices_to_compute, chosen_dishes)
    return chosen_dishes
