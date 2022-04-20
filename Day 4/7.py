# find maximum and minimum value in a given list of tuples

def min_and_max(list_items):
    sorted_list = sorted(list_items, key=lambda x:x)
    min_val = min(sorted_list)
    max_val = max(sorted_list)

    return max_val, min_val

print(min_and_max([56, 78, 456, 4, 98, 34]))