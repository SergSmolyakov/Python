from random import randint
lst = [randint(1, 9) for i in range(20)]

def selection(lst):
    for i, e in enumerate(lst):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst
print(lst)