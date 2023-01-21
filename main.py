from typing import Hashable, Any


def merge_values(key: Hashable, first_dict: dict, second_dict: dict) -> Any:
    first_elem = first_dict.get(key, None)
    second_elem = second_dict.get(key, None)
    if isinstance(first_elem, dict) and isinstance(second_elem, dict):
        return deep_merge(first_elem, second_elem)

    if isinstance(first_elem, list) and isinstance(second_elem, list):
        first_elem.extend(second_elem)
        return first_elem
    if isinstance(first_elem, list):
        first_elem.append(second_elem)
        return first_elem
    if isinstance(second_elem, list):
        res: list = [first_elem]
        res.extend(second_elem)
        return res

    return second_elem or first_elem


def deep_merge(first_dict: dict, second_dict: dict) -> dict:
    result: dict = {}
    keys: set = set(first_dict.keys()).union(second_dict.keys())
    for key in keys:
        result[key] = merge_values(key, first_dict, second_dict)

    return result
