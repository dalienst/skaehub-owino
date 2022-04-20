# sort a list of dictionaries using lambda

from turtle import color


list_of_dict_data = [
    {'name':'Mash Poa', 'price': 2500, 'color':'yellowgold'},
    {'name':'Dreamline', 'price': 2300, 'color':'blue'},
    {'name':'Tahmeed', 'price': 2000, 'color':'white'},
    {'name':'Modern Coast', 'price': 2400, 'color':'orange'}
]

#sorting using name
def sort_dict_data(dict_items):
    sorted_items = sorted(dict_items, key=lambda x:x['name'])
    return sorted_items

print(sort_dict_data(list_of_dict_data))