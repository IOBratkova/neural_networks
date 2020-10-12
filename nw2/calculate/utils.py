import copy


# Подсчёт схожести
def __help_gemini(letter_a, letter_b):
    t = 0
    for i in range(len(letter_a)):
        if letter_b[i] == letter_a[i]:
            t += 1
    return t


def copy_and_insert_one(lst):
    res = copy.deepcopy(lst)
    res.insert(0, 1)
    return res
