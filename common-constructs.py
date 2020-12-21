"""
This module illustrates common Python constructs - such as for, if - and common
data structures - such as list, dictionaries.
"""
for _ in range(6):
    print(_)

example_dict = {'apples': 5, 'oranges': 8, 'bananas': 13}
dict_to_list = list(example_dict)
print(dict_to_list)

dict_to_list = dict_to_list + ['pears']
print(dict_to_list)

print(sorted(dict_to_list))
