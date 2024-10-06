#!/usr/bin/env python3

# Name: Prasad Mistry
# Student Number: 111964193
# Student Email: pmistry21@myseneca.ca
# Course: OPS445
# Section: ZAA
# Semester: Fall 2024
# Date: 2024/10/05

my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    update_list = ordered_list[-1] + 1
    ordered_list.append(update_list)

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for i in items_to_remove:
        while i in ordered_list:
            ordered_list.remove(i)


# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)