import copy


def copy_and_insert_one(list):
    result = copy.deepcopy(list)
    result.insert(0, 1)
    return result


def make_bipolar_list(list):
    return [-1 if not el else 1 for el in list]
