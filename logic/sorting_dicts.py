from operator import itemgetter


def sort_by_value_itemgetter(passed_dict: dict, value_index: int) -> dict:
    return dict(sorted(passed_dict.items(), key=itemgetter(value_index)))


def sort_dict_masses_lambda(passed_dict: dict, mass_index=1, exponent_index=1) -> dict:
    return dict(
        sorted(passed_dict.items(), key=lambda x: x[mass_index][exponent_index])
    )
