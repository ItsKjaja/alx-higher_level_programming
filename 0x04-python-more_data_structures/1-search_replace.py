#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for i in range(len(my_list)):
        value = my_list[i]
        if value == search:
            value = replace
        new_list.append(value)
    return new_list
