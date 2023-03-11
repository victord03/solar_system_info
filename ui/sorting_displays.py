

def sort_dict_by_value(passed_dict: dict, value_index: int) -> dict:
    return dict(sorted(passed_dict.items(), key=lambda x: x[value_index]))
