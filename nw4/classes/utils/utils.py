import copy


def copy_and_insert_one(lst):
    result = copy.deepcopy(lst)
    result.insert(0, 1)
    return result
