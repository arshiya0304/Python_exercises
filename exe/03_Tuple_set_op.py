def str(strings):
    t = tuple(strings)
    uni_items = set(t)
    return sorted(uni_items)
items = input("Enter strings separated by space: ").split()

lst_str = str(items)
print(lst_str)
